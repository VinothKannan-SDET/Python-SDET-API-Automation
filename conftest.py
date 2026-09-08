import pytest
from api.clients.auth_client import AuthClient
from api.clients.base_client import BaseClient
from api.clients.booking_client import BookingClient
from utilities.config_reader import ConfigReader
from utilities.allure_metadata import write_allure_metadata


@pytest.fixture
def client():
    return BaseClient()


@pytest.fixture
def config():
    return ConfigReader()


@pytest.fixture
def auth_client(client):
    return AuthClient(client)


@pytest.fixture
def booking_client(client):
    return BookingClient(client)


@pytest.fixture
def auth_token(auth_client, config):
    response = auth_client.generate_token(config.auth_username, config.auth_password)
    assert response.status_code == 200
    token = response.json().get("token")
    assert token, "Authentication token was not returned"
    return token


def pytest_sessionfinish(session, exitstatus):
    write_allure_metadata()




def pytest_runtest_setup(item):
    import allure
    marker_names = {m.name for m in item.iter_markers()}
    allure.dynamic.parent_suite("Python API Automation")
    allure.dynamic.suite(item.fspath.basename)
    for name in ("smoke", "regression", "negative", "contract", "bdd"):
        if name in marker_names:
            allure.dynamic.tag(name)
    if "negative" in marker_names:
        allure.dynamic.severity(allure.severity_level.NORMAL)
    elif "smoke" in marker_names:
        allure.dynamic.severity(allure.severity_level.CRITICAL)
    else:
        allure.dynamic.severity(allure.severity_level.NORMAL)
