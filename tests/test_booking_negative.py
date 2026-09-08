import pytest
import allure
from test_data.booking_data import INVALID_BOOKING_DATA
from test_data.negative_booking_data import MISSING_FIRSTNAME_DATA, INVALID_PRICE_DATA
from utilities.assertions import assert_status_code, assert_response_is_json


@pytest.mark.parametrize("invalid_booking_id", [999999, 999998])
@pytest.mark.negative
@pytest.mark.regression
@allure.title("Verify GET booking with invalid booking ID")
def test_get_booking_invalid_id(booking_client, invalid_booking_id):
    response = booking_client.get_booking(invalid_booking_id)
    assert_status_code(response, 404)
    assert response.text == "Not Found"


@pytest.mark.parametrize(
    "invalid_booking_data, expected_status_code",
    [
        pytest.param(INVALID_BOOKING_DATA, 500, id="missing_required_fields"),
        pytest.param(MISSING_FIRSTNAME_DATA, 500, id="missing_firstname"),
        pytest.param(INVALID_PRICE_DATA, 200, id="invalid_price_type"),
    ],
)
@pytest.mark.negative
@pytest.mark.regression
def test_create_booking_invalid_payload(
    booking_client,
    invalid_booking_data,
    expected_status_code
):
    response = booking_client.create_booking(invalid_booking_data)
    assert_status_code(response, expected_status_code)


@pytest.mark.parametrize("username,password", [
    pytest.param("InvalidUser", "InvalidPassword", id="invalid_both"),
    pytest.param("admin", "InvalidPassword", id="invalid_password"),
])
@pytest.mark.negative
@pytest.mark.regression
@allure.title("Verify authentication rejects invalid credentials")
def test_generate_auth_token_invalid_credentials(auth_client, username, password):
    response = auth_client.generate_token(username, password)
    assert_status_code(response, 200)
    assert_response_is_json(response)
    assert response.json()["reason"] == "Bad credentials"
