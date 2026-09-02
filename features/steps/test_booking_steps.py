import pytest
from pytest_bdd import scenarios, given, when, then

from schemas.create_booking_schema import CREATE_BOOKING_RESPONSE_SCHEMA
from test_data.booking_data import VALID_BOOKING_DATA
from utilities.assertions import assert_status_code, assert_response_is_json, assert_json_field_exists, \
    assert_nested_json_value
from utilities.schema_validator import validate_schema

scenarios("../booking/booking.feature")

@pytest.fixture
def booking_context():
    return {}

@given("I have valid booking details")
def valid_booking_details(booking_context):
    booking_context["data"] = VALID_BOOKING_DATA

@when("I create a booking")
def create_booking(booking_context, booking_client):
    response = booking_client.create_booking(booking_context["data"])
    booking_context["response"] = response

@then("the booking should be created successfully")
def verify_booking_details(booking_context):
    response = booking_context["response"]
    assert_status_code(response, 200)

@then("the booking response should contain the expected details")
def verify_booking_details(booking_context):
    response = booking_context["response"]

    assert_response_is_json(response)
    response_data = response.json()

    validate_schema(response_data, CREATE_BOOKING_RESPONSE_SCHEMA)

    assert_json_field_exists(response_data, "bookingid")
    assert_json_field_exists(response_data, "booking")
    assert_nested_json_value(response_data, "booking.firstname",
                             booking_context["data"]["firstname"])
    assert_nested_json_value(response_data, "booking.lastname",
                             booking_context["data"]["lastname"])
    assert_nested_json_value(response_data, "booking.totalprice",
                             booking_context["data"]["totalprice"])
    assert_nested_json_value(response_data, "booking.depositpaid", True)





