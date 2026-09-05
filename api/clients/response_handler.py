"""
Common response handling utilities.
"""


class ResponseHandler:
    """
    Provides reusable operations for handling API responses.
    """

    @staticmethod
    def get_json(response):
        """
        Return the response body as JSON.

        :param response: requests.Response object
        :return: Parsed JSON response
        """
        return response.json()

    @staticmethod
    def get_text(response):
        """
        Return the response body as text.

        :param response: requests.Response object
        :return: Response text
        """
        return response.text

    @staticmethod
    def get_status_code(response):
        """
        Return the HTTP status code.

        :param response: requests.Response object
        :return: HTTP status code
        """
        return response.status_code

    @staticmethod
    def is_json(response):
        """
        Check whether the response contains a JSON content type.

        :param response: requests.Response object
        :return: True when response is JSON, otherwise False
        """
        content_type = response.headers.get("Content-Type", "")
        return "application/json" in content_type