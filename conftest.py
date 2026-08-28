import pytest
from api.clients.auth_client import AuthClient
from api.clients.base_client import BaseClient
from api.clients.booking_client import BookingClient
from utilities.config_reader import ConfigReader


@pytest.fixture
def client():
    """
    Provide a BaseClient instance for API tests.
    """
    return BaseClient()

@pytest.fixture
def config():
    """
    Provide ConfigReader instance to tests.

    :return: ConfigReader object
    """
    return ConfigReader()

@pytest.fixture
def auth_client(client):
    """
    Provide an AuthClient using the existing BaseClient.

    :param client: BaseClient fixture
    :return: AuthClient instance
    """
    return AuthClient(client)

@pytest.fixture
def booking_client(client):
    """
    Provide BookingClient using the existing BaseClient.

    :param client: BaseClient fixture
    :return: BookingClient object
    """
    return BookingClient(client)

@pytest.fixture
def auth_token(auth_client, config):
    """
    Generate and return an authentication token.

    :param auth_client: AuthClient fixture
    :param config: ConfigReader fixture
    :return: Authentication token
    """

    response = auth_client.generate_token(
        config.auth_username,
        config.auth_password
    )

    assert response.status_code == 200

    response_data = response.json()

    assert "token" in response_data

    return response_data["token"]