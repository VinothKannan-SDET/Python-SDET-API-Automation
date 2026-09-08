import allure
import pytest
from pytest_bdd import scenarios, given, when, then
from utilities.assertions import assert_status_code, assert_response_is_json, assert_json_value

pytestmark = pytest.mark.bdd
scenarios("../authentication/authentication.feature")


@pytest.fixture
def auth_context():
    return {}


@given("I have valid authentication credentials")
def valid_credentials(auth_context, config):
    auth_context["username"] = config.auth_username
    auth_context["password"] = config.auth_password


@given("I have invalid authentication credentials")
def invalid_credentials(auth_context):
    auth_context["username"] = "InvalidUser"
    auth_context["password"] = "InvalidPassword"


@when("I request an authentication token")
def request_token(auth_context, auth_client):
    auth_context["response"] = auth_client.generate_token(
        auth_context["username"], auth_context["password"]
    )


@then("the authentication request should be successful")
def auth_success(auth_context):
    assert_status_code(auth_context["response"], 200)
    assert_response_is_json(auth_context["response"])


@then("an authentication token should be returned")
def token_returned(auth_context):
    assert_json_value(auth_context["response"].json(), "token", auth_context["response"].json().get("token"))
    assert auth_context["response"].json().get("token")


@then("the authentication request should be unsuccessful")
def auth_unsuccessful(auth_context):
    assert_status_code(auth_context["response"], 200)
    assert_response_is_json(auth_context["response"])


@then('the authentication reason should be "Bad credentials"')
def auth_reason(auth_context):
    assert_json_value(auth_context["response"].json(), "reason", "Bad credentials")
