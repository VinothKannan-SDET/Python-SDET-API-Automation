import requests

from utilities.config_reader import ConfigReader

from utilities.logger import get_logger

class BaseClient:
    logger = get_logger(__name__)
    """
    Reusable base client for API communication.

    Provides common HTTP methods such as GET, POST, PUT,
    PATCH and DELETE.
    """
    def __init__(self):
        """
        Initialize the API client.
        """
        self.config = ConfigReader()

        self.base_url = self.config.base_url
        self.timeout = self.config.timeout

        # Create a reusable HTTP session
        self.session = requests.Session()

    def get(self, endpoint, params=None, headers=None):
        """
        Send a GET request.

        :param endpoint: API endpoint path
        :param params: Query parameters
        :param headers: Request headers
        :return: Response object
        """
        url = f"{self.base_url}{endpoint}"
        self.logger.info("GET request: %s", url)

        response = self.session.get(
            url=url,
            params=params,
            headers=headers,
            timeout=self.timeout
        )

        self.logger.info("GET response %s", response.status_code)

        return response

    def post(self, endpoint, json=None, params=None, headers=None):
        """
        Send a POST request.

        :param endpoint: API endpoint path
        :param data: JSON request body
        :param params: Query parameters
        :param headers: Request headers
        :return: Response object
        """
        url = f"{self.base_url}{endpoint}"

        self.logger.info("POST request: %s", url)
        response = self.session.post(
            url=url,
            json=json,
            params=params,
            headers=headers,
            timeout=self.timeout
        )
        self.logger.info("POST response %s", response.status_code)
        return response

    def put(self, endpoint, json=None, params=None, headers=None):
        """
        Send a PUT request.

        :param endpoint: API endpoint path
        :param data: JSON request body
        :param params: Query parameters
        :param headers: Request headers
        :return: Response object
        """
        url = f"{self.base_url}{endpoint}"
        self.logger.info("PUT request: %s", url)

        response = self.session.put(
            url=f"{self.base_url}{endpoint}",
            json=json,
            params=params,
            headers=headers,
            timeout=self.timeout
        )
        self.logger.info("PUT response %s", response.status_code)
        return response

    def patch(self, endpoint, json=None, params=None, headers=None):
        """
        Send a PATCH request.

        :param endpoint: API endpoint path
        :param json: JSON request body
        :param params: Query parameters
        :param headers: Request headers
        :return: Response object
        """
        url = f"{self.base_url}{endpoint}"
        self.logger.info("PATCH request: %s", url)

        response = self.session.patch(
            url=url,
            json=json,
            params=params,
            headers=headers,
            timeout=self.timeout
        )
        self.logger.info("PATCH response %s", response.status_code)
        return response

    def delete(self, endpoint, params=None, headers=None):
        """
        Send a DELETE request.

        :param endpoint: API endpoint path
        :param params: Query parameters
        :param headers: Request headers
        :return: Response object
        """
        url = f"{self.base_url}{endpoint}"
        self.logger.info("DELETE request: %s", url)

        response = self.session.delete(
            url=url,
            params=params,
            headers=headers,
            timeout=self.timeout
        )
        self.logger.info("DELETE response %s", response.status_code)
        return response