class ResponseHandler:
    """
    Common utilities for handling API responses.
    """

    @staticmethod
    def get_json(response):
        """
        Return response body as JSON.

        :param response: Requests response object
        :return: JSON response body
        """

        return response.json()