import allure
import pytest

from test_data.booking_data import INVALID_BOOKING_DATA
from utilities.api_utils import attach_response
from utilities.assertions import assert_status_code


@allure.title("Verify GET booking with invalid booking ID")
def test_get_booking_invalid_id(booking_client):
    """
    Verify that GET booking returns 404 for a non-existing booking ID.
    """

    invalid_booking_id = 999999

    response = booking_client.get_booking(invalid_booking_id)

    attach_response(response)
    assert_status_code(response, 404)
    assert response.text == "Not Found"

@allure.title("Verify create booking with invalid payload")
@pytest.mark.parametrize("invalid_booking_data", [
    pytest.param(INVALID_BOOKING_DATA, id = "Missing_required_fields")
])
def test_create_booking_invalid_payload(booking_client, invalid_booking_data):
    """
    Verify that booking creation handles an invalid payload.
    """

    # invalid_booking_data = {
    #     "firstname": "John",
    # }

    response = booking_client.create_booking(invalid_booking_data)

    attach_response(response)
    assert_status_code(response, 500)
    assert response.text == "Internal Server Error"

@allure.title("Verify authentication with invalid credentials")
def test_generate_auth_token_invalid_credentials(auth_client):
    """
    Verify that authentication fails with invalid credentials.
    """

    response = auth_client.generate_token(
        "InvalidUser",
        "InvalidPassword"
    )

    attach_response(response)
    assert_status_code(response, 200)

    response_data = response.json()

    assert response_data["reason"] == "Bad credentials"
