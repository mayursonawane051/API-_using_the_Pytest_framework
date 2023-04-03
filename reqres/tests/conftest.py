import pytest


@pytest.fixture(scope='session')
def setup():
    """
    There is no setup required for the server 'reqres' as these are opensource API.
    But just for future enhancements keeping this setup file in the conftest.
    """
    print("Started the execution..")
    base_url = "https://reqres.in/api/users"
    yield
    print(" Automation execution is completed..!")
