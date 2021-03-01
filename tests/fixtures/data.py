import pytest
from pytest import fixture
import os


@fixture(scope='session')
def user():
    return {
        'user_id': os.getenv('TEST_USER_ID', 0),
        'client_app': 'testsuite',
        'global_id': os.getenv('TEST_USER_GLOBAL_ID', None)
    }