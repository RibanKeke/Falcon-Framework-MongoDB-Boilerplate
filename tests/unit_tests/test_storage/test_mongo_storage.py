"""
Author: Robert Banziziki
"""
from bson import ObjectId
from mongoengine import Document
from mongoengine.fields import StringField

from app.storage.mongo_storage import MongoStorage


class TestDoc(Document):
    name = StringField(required=True)

class TestMongoStorage(object):
    """
    Test the mongo_db_storage
    """

    def test_connection_passed(self, config):
        MongoStorage(**config)
        test_item = TestDoc(name='Test').save()
        assert isinstance(test_item.id, ObjectId)

