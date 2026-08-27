import pytest
from api.clients.base_client import BaseClient

@pytest.fixture
def client():
    """
    Provide a BaseClient instance for API tests.
    """
    return BaseClient()