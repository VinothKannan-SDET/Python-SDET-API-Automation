from api.clients.base_client import BaseClient
import allure

from api.endpoints.auth_endpoints import AUTHENTICATION
from utilities import logger


class AuthClient:
    """
    Handles API authentication operations.
    """
    def __init__(self, client):
        """
        Initialize AuthClient.

        :param client: Existing BaseClient instance
        """
        self.client = client

    @allure.step("Generate authentication token")
    def generate_token(self, username, password):
        """
        Generate authentication token using API credentials.

        :param username: API username
        :param password: API password
        :return: Authentication response
        """

        payload = {
            "username": username,
            "password": password
        }

        return self.client.post(
            AUTHENTICATION,
            json=payload
        )