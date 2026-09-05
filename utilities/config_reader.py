from configparser import ConfigParser
import os

from dotenv import load_dotenv

class ConfigReader:
    """
    Read framework configuration and environment variables.
    """
    def __init__(self):
        load_dotenv()
        self.config = ConfigParser()
        self.config.read("config/config.ini")

    @property
    def base_url(self):
        """Return the configured API base URL."""
        return self.config["application"]["base_url"]

    @property
    def timeout(self):
        """Return the API request timeout."""
        return int(self.config["execution"]["timeout"])

    @property
    def retry_count(self):
        """Return the test retry count."""
        return int(self.config["execution"]["retry_count"])

    @property
    def auth_username(self):
        """Return API username from environment variables."""
        username = os.getenv("AUTH_USERNAME")

        if not username:
            raise RuntimeError(
                "AUTH_USERNAME environment variable is not configured."
            )

        return username

    @property
    def auth_password(self):
        """Return API password from environment variables."""
        password = os.getenv("AUTH_PASSWORD")

        if not password:
            raise RuntimeError(
                "AUTH_PASSWORD environment variable is not configured."
            )

        return password
