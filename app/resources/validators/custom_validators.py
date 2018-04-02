"""
Author:
Date:
"""
from bson import  ObjectId
from bson.errors import InvalidId
from webargs import ValidationError


def is_a_valid_object_id(val):
    try:
        ObjectId(val)
    except InvalidId as exc:
        raise ValidationError(str(exc), status_code=400)
