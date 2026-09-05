import allure
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from schemas.create_booking_schema import CREATE_BOOKING_RESPONSE_SCHEMA
from test_data.booking_data import VALID_BOOKING_DATA
from utilities.assertions import assert_response_is_json, assert_status_code, assert_nested_json_value
from utilities.booking_assertions import (
    assert_booking_created,
    assert_booking_details
)
pytestmark = pytest.mark.bdd
from utilities.schema_validator import validate_schema
from copy import deepcopy

# Link this Python step-definition file with the booking.feature file.
scenarios("../booking/booking_creation.feature")
scenarios("../booking/booking_retrieval.feature")
scenarios("../booking/booking_update.feature")
scenarios("../booking/booking_deletion.feature")

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
    booking_context["data"] = deepcopy(VALID_BOOKING_DATA)

@allure.step("Create booking")
@when("I create a booking")
def create_booking(booking_context, booking_client):
    """
    Create a booking using the prepared booking data.
    """
    response = booking_client.create_booking(booking_context["data"])
    booking_context["response"] = response
    assert_status_code(response, 200)
    assert_response_is_json(response)

    response_data = response.json()

    booking_context["booking_id"] = response_data["bookingid"]

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

    assert_status_code(response, 200)
    assert_response_is_json(response)

    response_data = response.json()

    booking_context["booking_id"] = response_data["bookingid"]

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

@allure.step("Verify booking first name is {firstname}")
@then(parsers.parse(
    'the booking first name should be "{firstname}"'))
def verify_booking_first_name(booking_context, firstname):

    response_data = booking_context["response"].json()

    assert_nested_json_value(response_data,"booking.firstname",firstname)

@allure.step("Retrieve the created booking")
@when("I retrieve the created booking")
def retrieve_created_booking(booking_context, booking_client):

    booking_id = booking_context["booking_id"]

    response = booking_client.get_booking(booking_id)

    booking_context["get_response"] = response

@allure.step("Verify booking was retrieved successfully")
@then("the booking should be retrieved successfully")
def verify_booking_retrieved(booking_context):

    response = booking_context["get_response"]

    assert_status_code(response, 200)

    assert_response_is_json(response)

@allure.step("Verify retrieved booking matches booking details")
@then("the retrieved booking should match the booking details")
def verify_retrieved_booking_details(booking_context):

    response_data = (booking_context["get_response"].json())

    booking_data = booking_context["data"]

    assert_nested_json_value(response_data, "firstname", booking_data["firstname"])

    assert_nested_json_value(response_data, "lastname", booking_data["lastname"])

    assert_nested_json_value(response_data, "totalprice", booking_data["totalprice"])

    assert_nested_json_value(response_data, "depositpaid", booking_data["depositpaid"])

@allure.step("Prepare updated booking details")
@given("I have updated booking details")
def updated_booking_details(booking_context):

    booking_context["updated_data"] = {
        "firstname": "Robert",
        "lastname": "Wilson",
        "totalprice": 350,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-07"
        },
        "additionalneeds": "Lunch"
    }

@allure.step("Update the created booking")
@when("I update the created booking")
def update_created_booking(booking_context, booking_client,
        auth_token):

    booking_id = booking_context["booking_id"]

    update_data = booking_context["updated_data"]

    response = booking_client.update_booking(booking_id, update_data, auth_token)

    booking_context["update_response"] = response

@allure.step("Verify booking was updated successfully")
@then("the booking should be updated successfully")
def verify_booking_updated(booking_context):

    response = booking_context["update_response"]

    assert_status_code(response,200)

    assert_response_is_json(response)

@allure.step("Verify updated booking details")
@then("the updated booking should match the updated details")
def verify_updated_booking_details(booking_context):

    response_data = (booking_context["update_response"].json())

    update_data = booking_context["updated_data"]

    assert_nested_json_value(response_data, "firstname", update_data["firstname"])

    assert_nested_json_value(response_data, "lastname", update_data["lastname"])

    assert_nested_json_value(response_data, "totalprice", update_data["totalprice"])

    assert_nested_json_value(response_data, "depositpaid", update_data["depositpaid"])

@allure.step("Delete the created booking")
@when("I delete the created booking")
def delete_created_booking(booking_context, booking_client,
                           auth_token):

    booking_id = booking_context["booking_id"]

    response = booking_client.delete_booking(booking_id, auth_token)

    booking_context["delete_response"] = response

@allure.step("Verify booking was deleted successfully")
@then("the booking should be deleted successfully")
def verify_booking_deleted(booking_context):

    response = booking_context["delete_response"]

    assert_status_code(response, 201)

@allure.step("Verify deleted booking no longer exists")
@then("the deleted booking should no longer exist")
def verify_booking_no_longer_exists(booking_context,booking_client):

    booking_id = booking_context["booking_id"]

    response = booking_client.get_booking(booking_id)

    assert_status_code(response,404)



