import pytest
import allure
from test_data.booking_factory import (
    create_valid_booking,
    create_booking_with_breakfast,
    create_booking_without_deposit,
    create_booking_with_high_price,
)
from test_data.boundary_booking_data import MINIMUM_PRICE_BOOKING, HIGH_VALUE_BOOKING
from utilities.assertions import assert_status_code, assert_response_is_json, assert_json_field_exists
from utilities.booking_assertions import assert_booking_details


@pytest.mark.smoke
@pytest.mark.regression
@allure.title("Verify booking service health endpoint")
def test_ping_health(client):
    response = client.get("/ping")
    assert_status_code(response, 201)
    assert response.text == "Created"


@pytest.mark.regression
@pytest.mark.contract
@allure.title("Verify get all bookings returns a JSON list")
def test_get_all_bookings_returns_list(booking_client):
    response = booking_client.get_all_bookings()
    assert_status_code(response, 200)
    assert_response_is_json(response)
    assert isinstance(response.json(), list)


@pytest.mark.regression
@pytest.mark.contract
@allure.title("Verify booking list entries contain booking IDs")
def test_get_all_bookings_contains_ids(booking_client):
    response = booking_client.get_all_bookings()
    assert_status_code(response, 200)
    for item in response.json()[:10]:
        assert "bookingid" in item


@pytest.mark.regression
@allure.title("Verify booking can be filtered by first name")
def test_get_bookings_by_firstname(booking_client):
    data = create_valid_booking(firstname="FilterFirst", lastname="FilterLast").to_dict()
    create_response = booking_client.create_booking(data)
    booking_id = create_response.json()["bookingid"]
    response = booking_client.get_all_bookings(params={"firstname": "FilterFirst"})
    assert_status_code(response, 200)
    assert any(item.get("bookingid") == booking_id for item in response.json())


@pytest.mark.parametrize("factory", [
    pytest.param(create_booking_with_breakfast, id="with_breakfast"),
    pytest.param(create_booking_without_deposit, id="without_deposit"),
    pytest.param(create_booking_with_high_price, id="high_price"),
])
@pytest.mark.regression
@allure.title("Verify booking creation using reusable factory data")
def test_create_booking_factory_variants(booking_client, factory):
    data = factory().to_dict()
    response = booking_client.create_booking(data)
    assert_status_code(response, 200)
    assert_response_is_json(response)
    booking_id = response.json()["bookingid"]
    assert_booking_details(booking_client.get_booking(booking_id), data)


@pytest.mark.parametrize("booking_data", [
    pytest.param(MINIMUM_PRICE_BOOKING, id="minimum_price"),
    pytest.param(HIGH_VALUE_BOOKING, id="high_value"),
])
@pytest.mark.regression
@allure.title("Verify booking creation boundary values")
def test_create_booking_boundary_values(booking_client, booking_data):
    response = booking_client.create_booking(booking_data)
    assert_status_code(response, 200)
    assert_response_is_json(response)


@pytest.mark.negative
@pytest.mark.regression
@allure.title("Verify update is rejected with invalid token")
def test_update_booking_invalid_token(booking_client):
    create_response = booking_client.create_booking(create_valid_booking().to_dict())
    booking_id = create_response.json()["bookingid"]
    response = booking_client.update_booking(
        booking_id, create_valid_booking(firstname="Blocked").to_dict(), "invalid-token"
    )
    assert_status_code(response, 403)


@pytest.mark.negative
@pytest.mark.regression
@allure.title("Verify patch is rejected with invalid token")
def test_patch_booking_invalid_token(booking_client):
    create_response = booking_client.create_booking(create_valid_booking().to_dict())
    booking_id = create_response.json()["bookingid"]
    response = booking_client.patch_booking(booking_id, {"firstname": "Blocked"}, "invalid-token")
    assert_status_code(response, 403)


@pytest.mark.negative
@pytest.mark.regression
@allure.title("Verify delete is rejected with invalid token")
def test_delete_booking_invalid_token(booking_client):
    create_response = booking_client.create_booking(create_valid_booking().to_dict())
    booking_id = create_response.json()["bookingid"]
    response = booking_client.delete_booking(booking_id, "invalid-token")
    assert_status_code(response, 403)


@pytest.mark.regression
@allure.title("Verify PATCH changes only selected booking fields")
def test_patch_single_field_preserves_other_fields(booking_client, auth_token):
    original = create_valid_booking(
        firstname="PatchFirst", lastname="PatchLast", totalprice=175
    ).to_dict()
    create_response = booking_client.create_booking(original)
    booking_id = create_response.json()["bookingid"]
    response = booking_client.patch_booking(booking_id, {"firstname": "Patched"}, auth_token)
    assert_status_code(response, 200)
    data = response.json()
    assert data["firstname"] == "Patched"
    assert data["lastname"] == "PatchLast"
    assert data["totalprice"] == 175
