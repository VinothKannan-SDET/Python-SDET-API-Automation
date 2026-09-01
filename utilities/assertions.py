

def assert_status_code(response, expected_status_code):
    """
    Validate the HTTP response status code.

    :param response: requests.Response object
    :param expected_status_code: Expected HTTP status code
    """
    actual_status_code = response.status_code
    assert actual_status_code == expected_status_code, (
        f"Expected status code {expected_status_code},"
        f"but received {actual_status_code}"
    )

def assert_json_field_exists(response_data, field_name):
    """
    Validate that a field exists in a JSON response.

    :param response_data: Parsed JSON response
    :param field_name: Field that must exist
    """

    assert field_name in response_data, (
        f"Expected field '{field_name}' "
        f"was not found in response"
    )

def assert_json_value(response_data, field_name, expected_value):
    """
    Validate the value of a JSON response field.

    :param response_data: Parsed JSON response
    :param field_name: JSON field name
    :param expected_value: Expected value
    """

    actual_value = response_data.get(field_name)

    assert actual_value == expected_value, (
        f"Expected '{field_name}' to be "
        f"'{expected_value}', but received '{actual_value}'"
    )

def assert_nested_json_value(
    response_data,
    field_path,
    expected_value
):
    """
    Validate a value using a dot-separated JSON field path.

    Example:
        booking.firstname

    :param response_data: Parsed JSON response
    :param field_path: Dot-separated field path
    :param expected_value: Expected value
    """

    current_value = response_data

    for field in field_path.split("."):
        assert isinstance(current_value, dict), (
            f"Expected '{field}' to exist in JSON object"
        )

        assert field in current_value, (
            f"Expected field '{field}' "
            f"was not found in response"
        )

        current_value = current_value[field]

    assert current_value == expected_value, (
        f"Expected '{field_path}' to be "
        f"'{expected_value}', "
        f"but received '{current_value}'"
    )

def assert_response_is_json(response):
    """
    Validate that the API response contains JSON data.
    """

    try:
        response.json()
    except ValueError:
        raise AssertionError(
            "Expected JSON response, but response "
            "could not be parsed as JSON."
        )