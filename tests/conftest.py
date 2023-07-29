import pytest
from net_hawk_poc.api import settings

@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
   settings.configure(FORCE_ENV_FOR_DYNACONF="testing")
