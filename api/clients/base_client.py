import requests

from utilities.config_reader import ConfigReader

class BaseClient:
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
        return self.session.get(
            url=f"{self.base_url}{endpoint}",
            params=params,
            headers=headers,
            timeout=self.timeout
        )

    def post(self, endpoint, data=None, params=None, headers=None):
        """
        Send a POST request.

        :param endpoint: API endpoint path
        :param data: JSON request body
        :param params: Query parameters
        :param headers: Request headers
        :return: Response object
        """
        return self.session.post(
            url=f"{self.base_url}{endpoint}",
            json=data,
            params=params,
            headers=headers,
            timeout=self.timeout
        )
    def put(self, endpoint, data=None, params=None, headers=None):
        """
        Send a PUT request.

        :param endpoint: API endpoint path
        :param data: JSON request body
        :param params: Query parameters
        :param headers: Request headers
        :return: Response object
        """
        return self.session.put(
            url=f"{self.base_url}{endpoint}",
            json=data,
            params=params,
            headers=headers,
            timeout=self.timeout
        )

    def patch(self, endpoint, data=None, params=None, headers=None):
        """
        Send a PATCH request.

        :param endpoint: API endpoint path
        :param data: JSON request body
        :param params: Query parameters
        :param headers: Request headers
        :return: Response object
        """

        return self.session.patch(
            url=f"{self.base_url}{endpoint}",
            json=data,
            params=params,
            headers=headers,
            timeout=self.timeout
        )

    def delete(self, endpoint, params=None, headers=None):
        """
        Send a DELETE request.

        :param endpoint: API endpoint path
        :param params: Query parameters
        :param headers: Request headers
        :return: Response object
        """

        return self.session.delete(
            url=f"{self.base_url}{endpoint}",
            params=params,
            headers=headers,
            timeout=self.timeout
        )