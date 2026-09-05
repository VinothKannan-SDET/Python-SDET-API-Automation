"""
Reusable authentication header utilities.
"""


def token_header(token):
    """
    Build the authentication header required by the Booking API.

    :param token: Authentication token
    :return: Dictionary containing the authentication header
    """
    return {
        "Cookie": f"token={token}"
    }