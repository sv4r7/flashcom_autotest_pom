import pytest


@pytest.fixture()
def set_up():
    print('Start Test')
    yield
    print('Finish Test')
