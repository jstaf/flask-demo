'''
Pre-test setup functions.
'''

import pytest
from api import api


@pytest.fixture
def client():
    '''
    Can't do tests without an app to test against, can we?
    '''
    yield api.app.test_client()
