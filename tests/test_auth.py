import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_generate_auth_token(auth_client, config):
    """
    Verify that the authentication API generates a token.
    """

    response = auth_client.generate_token(
        config.auth_username,
        config.auth_password
    )

    assert response.status_code == 200

    response_data = response.json()

    assert "token" in response_data