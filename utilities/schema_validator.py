from jsonschema import validate

def validate_schema(response_data, schema):
    """
    Validate API response data against the supplied JSON schema.

    :param response_data: Parsed JSON response
    :param schema: JSON schema definition
    :return: None if validation succeeds
    """

    validate(instance=response_data, schema=schema)