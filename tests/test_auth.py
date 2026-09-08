import pytest
import allure
from utilities.assertions import assert_status_code, assert_response_is_json


@pytest.mark.smoke
@pytest.mark.regression
@allure.title("Generate authentication token with valid credentials")
def test_generate_auth_token(auth_client, config):
    response = auth_client.generate_token(config.auth_username, config.auth_password)
    assert_status_code(response, 200)
    assert_response_is_json(response)
    token = response.json().get("token")
    assert token
