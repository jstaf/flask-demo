'''
Pre-test setup functions. Can't test without an app to test against, can we?
'''

import pytest
import tempfile
from api import api


@pytest.fixture(scope='session')
def client():
    # test database is a random tempfile
    _, tmp = tempfile.mkstemp(suffix='.db')
    api.app.config['db'] = 'sqlite:///' + tmp
    yield api.app.test_client()


@pytest.fixture(scope='session')
def db():
    return api.get_db()
