from utilities.config_reader import ConfigReader


def test_configuration():
    config = ConfigReader()

    assert config.base_url == "https://restful-booker.herokuapp.com"
    assert config.timeout == 10
    assert config.retry_count == 3