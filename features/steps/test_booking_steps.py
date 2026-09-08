import pytest
from copy import deepcopy
from pytest_bdd import scenarios, given, when, then, parsers
from test_data.booking_data import VALID_BOOKING_DATA
from test_data.booking_factory import create_updated_booking
from schemas.create_booking_schema import CREATE_BOOKING_RESPONSE_SCHEMA
from utilities.assertions import assert_response_is_json, assert_status_code, assert_nested_json_value
from utilities.booking_assertions import assert_booking_created, assert_created_booking_details, assert_booking_details
from utilities.schema_validator import validate_schema

pytestmark = pytest.mark.bdd
scenarios("../booking/booking_creation.feature")
scenarios("../booking/booking_retrieval.feature")
scenarios("../booking/booking_update.feature")
scenarios("../booking/booking_deletion.feature")


@pytest.fixture
def booking_context():
    return {}


@given("I have valid booking details")
def valid_booking_details(booking_context):
    booking_context["data"] = deepcopy(VALID_BOOKING_DATA)


@when("I create a booking")
def create_booking(booking_context, booking_client):
    response = booking_client.create_booking(booking_context["data"])
    booking_context["response"] = response
    assert_status_code(response, 200)
    assert_response_is_json(response)
    booking_context["booking_id"] = response.json()["bookingid"]


@when(parsers.parse('I create a booking with first name "{firstname}"'))
def create_booking_with_first_name(booking_context, booking_client, firstname):
    booking_context["data"]["firstname"] = firstname
    response = booking_client.create_booking(booking_context["data"])
    booking_context["response"] = response
    assert_status_code(response, 200)
    assert_response_is_json(response)
    booking_context["booking_id"] = response.json()["bookingid"]


@then("the booking should be created successfully")
def verify_booking_created(booking_context):
    assert_booking_created(booking_context["response"])


@then("the booking response should contain the expected details")
def verify_booking_details(booking_context):
    response = booking_context["response"]
    validate_schema(response.json(), CREATE_BOOKING_RESPONSE_SCHEMA)
    assert_created_booking_details(response, booking_context["data"])


@then(parsers.parse('the booking first name should be "{firstname}"'))
def verify_booking_first_name(booking_context, firstname):
    assert_nested_json_value(booking_context["response"].json(), "booking.firstname", firstname)


@when("I retrieve the created booking")
def retrieve_created_booking(booking_context, booking_client):
    booking_context["get_response"] = booking_client.get_booking(booking_context["booking_id"])


@then("the booking should be retrieved successfully")
def verify_booking_retrieved(booking_context):
    assert_status_code(booking_context["get_response"], 200)
    assert_response_is_json(booking_context["get_response"])


@then("the retrieved booking should match the booking details")
def verify_retrieved_booking_details(booking_context):
    assert_booking_details(booking_context["get_response"], booking_context["data"])


@given("I have updated booking details")
def updated_booking_details(booking_context):
    booking_context["updated_data"] = create_updated_booking().to_dict()


@when("I update the created booking")
def update_created_booking(booking_context, booking_client, auth_token):
    booking_context["update_response"] = booking_client.update_booking(
        booking_context["booking_id"], booking_context["updated_data"], auth_token
    )


@then("the booking should be updated successfully")
def verify_booking_updated(booking_context):
    assert_status_code(booking_context["update_response"], 200)
    assert_response_is_json(booking_context["update_response"])


@then("the updated booking should match the updated details")
def verify_updated_booking_details(booking_context):
    assert_booking_details(booking_context["update_response"], booking_context["updated_data"])


@when("I delete the created booking")
def delete_created_booking(booking_context, booking_client, auth_token):
    booking_context["delete_response"] = booking_client.delete_booking(
        booking_context["booking_id"], auth_token
    )


@then("the booking should be deleted successfully")
def verify_booking_deleted(booking_context):
    assert_status_code(booking_context["delete_response"], 201)


@then("the deleted booking should no longer exist")
def verify_booking_no_longer_exists(booking_context, booking_client):
    response = booking_client.get_booking(booking_context["booking_id"])
    assert_status_code(response, 404)
