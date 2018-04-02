"""
Author:
Date:
"""

import pytest

from app.models.user import User
from mongoengine.errors import ValidationError


class TestUser(object):
    """
    Class for testing the User mongo document
    """

    def test_create_user_passed(self, db):
        new_user = User(name='Adam', surname='Bradley').save()
        read_user = User.objects(name='Adam').first()
        assert new_user.id == read_user.id

    def test_create_user_failed_missing_surname(self, db):
        with pytest.raises(ValidationError) as val_err:
            User(name='Paul', surname=None).save()
            assert "Field is required: ['surname']" in val_err