import json
import allure
import pytest
from schemas.booking_schema import BOOKING_RESPONSE_SCHEMA
from schemas.create_booking_schema import CREATE_BOOKING_RESPONSE_SCHEMA
from test_data.booking_factory import create_valid_booking
from utilities.assertions import assert_status_code, assert_json_field_exists, assert_nested_json_value, \
    assert_response_is_json
from utilities.schema_validator import validate_schema
from test_data.booking_data import VALID_BOOKING_DATA, VALID_BOOKING_DATA_2


def test_get_booking(booking_client):
    """
    Verify that an existing booking can be retrieved.
    """
    response = booking_client.get_booking(1)
    assert_status_code(response, 200)

    assert_response_is_json(response)
    response_data = response.json()

    validate_schema(response_data, BOOKING_RESPONSE_SCHEMA)

    assert_json_field_exists(response_data, "firstname")
    assert_json_field_exists(response_data, "lastname")
    assert_json_field_exists(response_data, "bookingdates")


@pytest.mark.parametrize("firstname",
                         [pytest.param("John",id="firstname_John"),
                          pytest.param("David",id="firstname_David"),
                          pytest.param("Michael",id="firstname_Michael")])
def test_create_booking(booking_client, firstname):
    """
    Verify that a new booking can be created successfully.
    """

    booking_data = create_valid_booking(
        firstname=firstname
    ).to_dict()

    allure.attach(
        json.dumps(booking_data, indent=4),
        name="Request Payload",
        attachment_type=allure.attachment_type.JSON
    )

    response = booking_client.create_booking(booking_data)

    assert_status_code(response, 200)

    assert_response_is_json(response)
    response_data = response.json()

    validate_schema(response_data, CREATE_BOOKING_RESPONSE_SCHEMA)

    assert_json_field_exists(response_data, "bookingid")
    assert_json_field_exists(response_data, "booking")
    assert_nested_json_value(response_data, "booking.firstname", booking_data["firstname"])
    assert_nested_json_value(response_data, "booking.lastname", booking_data["lastname"])
    assert_nested_json_value(response_data, "booking.totalprice", booking_data["totalprice"])
    assert_nested_json_value(response_data, "booking.depositpaid", booking_data["depositpaid"])

def test_create_and_get_booking(booking_client):
    """
        Verify that a newly created booking can be retrieved
        using the dynamically generated booking ID.
        """

    booking_data = create_valid_booking(
        firstname="David",
        lastname="Miller",
        checkin="2026-09-10",
        checkout="2026-09-15"
    ).to_dict()

    # Step 1: Create a new booking
    create_response = booking_client.create_booking(booking_data)

    assert_status_code(create_response, 200)

    assert_response_is_json(create_response)
    create_response_data = create_response.json()

    # Step 2: Extract dynamically generated booking ID
    booking_id = create_response_data["bookingid"]

    assert booking_id is not None

    # Step 3: Retrieve the newly created booking
    get_response = booking_client.get_booking(booking_id)

    assert_status_code(get_response, 200)

    assert_response_is_json(get_response)
    get_response_data = get_response.json()

    # Step 4: Verify the retrieved booking data

    assert get_response_data["firstname"] == booking_data["firstname"]
    assert get_response_data["lastname"] == booking_data["lastname"]
    assert get_response_data["totalprice"] == booking_data["totalprice"]
    assert get_response_data["depositpaid"] is booking_data["depositpaid"]

    assert (
            get_response_data["bookingdates"]["checkin"]
            == booking_data["bookingdates"]["checkin"]
    )

    assert (
            get_response_data["bookingdates"]["checkout"]
            == booking_data["bookingdates"]["checkout"]
    )

def test_update_booking(booking_client, auth_token):
    """
      Verify that an existing booking can be fully updated.
      """

    # Step 1: Create a booking
    create_data = create_valid_booking(
        firstname="David",
        lastname="Miller",
        checkin="2026-09-10",
        checkout="2026-09-15"
    ).to_dict()

    create_response = booking_client.create_booking(create_data)

    assert_status_code(create_response, 200)
    assert_response_is_json(create_response)

    booking_id = create_response.json()["bookingid"]

    # Step 2: Prepare updated booking data
    update_data = create_valid_booking(
        firstname="Robert",
        lastname="Wilson",
        totalprice=350,
        depositpaid=False,
        checkin="2026-10-01",
        checkout="2026-10-07",
        additionalneeds="Lunch"
    ).to_dict()

    # Step 3: Update the booking
    update_response = booking_client.update_booking(
        booking_id, update_data, auth_token
    )

    assert_status_code(update_response, 200)
    assert_response_is_json(update_response)
    # Step 4: Verify response
    updated_data = update_response.json()

    assert updated_data["firstname"] == update_data["firstname"]
    assert updated_data["lastname"] == update_data["lastname"]
    assert updated_data["totalprice"] == update_data["totalprice"]
    assert updated_data["depositpaid"] is update_data["depositpaid"]

    # Step 5: Retrieve booking again
    get_response = booking_client.get_booking(
        booking_id
    )

    assert_status_code(get_response, 200)

    assert_response_is_json(get_response)
    retrieved_data = get_response.json()

    # Step 6: Verify persisted changes
    assert retrieved_data["firstname"] == update_data["firstname"]
    assert retrieved_data["lastname"] == update_data["lastname"]
    assert retrieved_data["totalprice"] == update_data["totalprice"]
    assert retrieved_data["depositpaid"] is update_data["depositpaid"]

def test_patch_booking(booking_client, auth_token):
    """
    Verify that selected booking fields can be partially updated.
    """
    # Step 1: Create a booking
    create_data = create_valid_booking(
        firstname="Michael",
        lastname="Brown",
        totalprice=250,
        checkin="2026-10-10",
        checkout="2026-10-15"
    ).to_dict()

    create_response = booking_client.create_booking(
        create_data
    )

    assert_status_code(create_response, 200)
    assert_response_is_json(create_response)

    booking_id = create_response.json()["bookingid"]

    # Step 2: Change only selected fields
    patch_data = {
        "firstname": "James",
        "totalprice": 450
    }

    patch_response = booking_client.patch_booking(
        booking_id,
        patch_data,
        auth_token
    )

    assert_status_code(patch_response, 200)
    assert_response_is_json(patch_response)

    # Step 3: Verify PATCH response
    patched_data = patch_response.json()

    assert patched_data["firstname"] == "James"
    assert patched_data["totalprice"] == 450

    # Step 4: Verify fields that were not patched remain unchanged
    assert patched_data["lastname"] == "Brown"
    assert patched_data["depositpaid"] is True

    # Step 5: GET the booking again
    get_response = booking_client.get_booking(
        booking_id
    )

    assert_status_code(get_response, 200)

    assert_response_is_json(get_response)
    retrieved_data = get_response.json()

    # Step 6: Verify persisted changes
    assert retrieved_data["firstname"] == "James"
    assert retrieved_data["totalprice"] == 450

    # Unchanged values should remain intact
    assert retrieved_data["lastname"] == "Brown"
    assert retrieved_data["depositpaid"] is True

def test_delete_booking(booking_client, auth_token):
    """
    Verify that an existing booking can be deleted successfully.
    """

    # Step 1: Create a booking
    create_data = create_valid_booking(
        firstname="Delete",
        lastname="Test",
        totalprice=300,
        checkin="2026-11-01",
        checkout="2026-11-05",
        additionalneeds="Dinner"
    ).to_dict()

    create_response = booking_client.create_booking(
        create_data
    )

    assert_status_code(create_response, 200)
    assert_response_is_json(create_response)

    # Step 2: Extract dynamically generated booking ID
    booking_id = create_response.json()["bookingid"]

    assert booking_id is not None

    # Step 3: Verify booking exists before deletion
    get_response = booking_client.get_booking(
        booking_id
    )

    assert_status_code(get_response, 200)

    # Step 4: Delete the booking
    delete_response = booking_client.delete_booking(
        booking_id,
        auth_token
    )

    assert_status_code(delete_response, 201)

    # Step 5: Verify booking no longer exists
    verify_response = booking_client.get_booking(
        booking_id
    )

    assert_status_code(verify_response, 404)
