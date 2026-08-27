import pytest
from api.clients.auth_client import AuthClient
from api.clients.base_client import BaseClient
from utilities.config_reader import ConfigReader


@pytest.fixture
def client():
    """
    Provide a BaseClient instance for API tests.
    """
    return BaseClient()

@pytest.fixture
def auth_client(client):
    """
    Provide an AuthClient using the existing BaseClient.

    :param client: BaseClient fixture
    :return: AuthClient instance
    """
    return AuthClient(client)

@pytest.fixture
def config():
    """
    Provide ConfigReader instance to tests.

    :return: ConfigReader object
    """
    return ConfigReader()
