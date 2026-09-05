import allure
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from schemas.create_booking_schema import CREATE_BOOKING_RESPONSE_SCHEMA
from test_data.booking_data import VALID_BOOKING_DATA
from utilities.assertions import assert_response_is_json
from utilities.booking_assertions import (
    assert_booking_created,
    assert_booking_details
)
pytestmark = pytest.mark.bdd
from utilities.schema_validator import validate_schema

# Link this Python step-definition file with the booking.feature file.
scenarios("../booking/booking.feature")

@pytest.fixture
def booking_context():
    """
    Stores data shared between BDD steps
    during a single scenario execution.
    """
    return {}

@allure.step("Prepare valid booking details")
@given("I have valid booking details")
def valid_booking_details(booking_context):
    """
    Prepare valid booking data for the scenario.
    """
    booking_context["data"] = VALID_BOOKING_DATA.copy()

@allure.step("Create booking")
@when("I create a booking")
def create_booking(booking_context, booking_client):
    """
    Create a booking using the prepared booking data.
    """
    response = booking_client.create_booking(booking_context["data"])
    booking_context["response"] = response

@allure.step("Create booking with first name: {firstname}")
@when(parsers.parse('I create a booking with first name "{firstname}"'))
def create_booking_with_first_name(booking_context, booking_client,
    firstname):
    """
    Create a booking using the firstname supplied
    by the Scenario Outline Examples table.
    """

    booking_context["data"]["firstname"] = firstname

    response = booking_client.create_booking(
        booking_context["data"]
    )

    booking_context["response"] = response

@allure.step("Verify booking was created successfully")
@then("the booking should be created successfully")
def verify_booking_created(booking_context):
    """
    Verify that the booking creation request
    returned the expected HTTP status.
    """
    response = booking_context["response"]

    assert_booking_created(response)

@allure.step("Validate booking response")
@then("the booking response should contain the expected details")
def verify_booking_details(booking_context):
    """
    Verify that the booking response contains
    the expected booking information.
    """
    response = booking_context["response"]

    assert_response_is_json(response)

    response_data = response.json()

    validate_schema(
        response_data,
        CREATE_BOOKING_RESPONSE_SCHEMA
    )

    assert_booking_details(
        response,
        booking_context["data"]
    )

@allure.step("Verify booking first name: {firstname}")
@then(parsers.parse('the booking first name should be "{firstname}"'))
def verify_booking_first_name(booking_context, firstname):
    """
    Verify that the API response contains
    the firstname supplied by the Scenario Outline.
    """
    response = booking_context["response"]
    response_data = response.json()

    # assert_nested_json_value(
    #     response_data,
    #     "booking.firstname",
    #     firstname
    # )




