"""
Author: Robert Banziziki
Date : 23 february 2018
"""
import pytest
from app import create_app
from falcon import testing

from app.storage.mongo_storage import MongoStorage

@pytest.fixture
def config():
    return {'db_name': 'test_db',
            'mongo_uri': 'mongodb://localhost/test_db'}

@pytest.fixture
def db(config):
    mongo_storage = MongoStorage(db_name=config['db_name'],
                                 mongo_uri=config['mongo_uri'])
    yield
    mongo_storage.db.drop_database(config['db_name'])


@pytest.fixture
def client(db):
    return testing.TestClient(create_app())