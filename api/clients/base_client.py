"""Reusable HTTP client abstraction for the automation framework."""

import requests
import allure

from utilities.api_utils import attach_request, attach_response
from utilities.config_reader import ConfigReader
from utilities.logger import get_logger


class BaseClient:
    """Owns HTTP transport, common configuration and Allure evidence."""

    logger = get_logger(__name__)

    def __init__(self):
        self.config = ConfigReader()
        self.base_url = self.config.base_url.rstrip("/")
        self.timeout = self.config.timeout
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def _request(self, method, endpoint, *, json=None, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        safe_headers = headers or {}
        self.logger.info("%s request: %s", method.upper(), url)
        attach_request(method, url, safe_headers, json, params)
        try:
            response = self.session.request(
                method=method.upper(), url=url, json=json, params=params,
                headers=headers, timeout=self.timeout
            )
        except requests.RequestException as exc:
            self.logger.error("%s request failed: %s", method.upper(), exc)
            raise
        self.logger.info("%s response %s", method.upper(), response.status_code)
        attach_response(response)
        return response

    @allure.step("HTTP GET: {endpoint}")
    def get(self, endpoint, params=None, headers=None):
        return self._request("GET", endpoint, params=params, headers=headers)

    @allure.step("HTTP POST: {endpoint}")
    def post(self, endpoint, json=None, params=None, headers=None):
        return self._request("POST", endpoint, json=json, params=params, headers=headers)

    @allure.step("HTTP PUT: {endpoint}")
    def put(self, endpoint, json=None, params=None, headers=None):
        return self._request("PUT", endpoint, json=json, params=params, headers=headers)

    @allure.step("HTTP PATCH: {endpoint}")
    def patch(self, endpoint, json=None, params=None, headers=None):
        return self._request("PATCH", endpoint, json=json, params=params, headers=headers)

    @allure.step("HTTP DELETE: {endpoint}")
    def delete(self, endpoint, params=None, headers=None):
        return self._request("DELETE", endpoint, params=params, headers=headers)
