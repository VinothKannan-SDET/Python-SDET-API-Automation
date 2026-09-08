"""Authentication-specific API client."""

import allure
from api.endpoints.auth_endpoints import AUTHENTICATION


class AuthClient:
    def __init__(self, client):
        self.client = client

    @allure.step("Generate authentication token")
    def generate_token(self, username, password):
        payload = {"username": username, "password": password}
        return self.client.post(AUTHENTICATION, json=payload)
