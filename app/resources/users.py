"""
Author: Robert Banziziki
Date: 23 february 2018
"""


import falcon
import app.util.json as json
from app.services.user_service.user_service import UserService

from webargs import fields
from webargs.falconparser import use_args
from app.resources.validators.custom_validators import is_a_valid_object_id


class UserResources(object):

    new_user_validation = {
        'name': fields.Str(required=True),
        'surname': fields.Str(required=True)
    }

    user_id_validation = {
        'user_id': fields.Str(validate=is_a_valid_object_id)
    }

    def __init__(self):
        self.user_service = UserService()

    def on_get(self, req, resp):
        resp.body = json.dumps([u.to_dict() for u in self.user_service.list_users()])

    @use_args(new_user_validation)
    def on_post(self, req, resp, args):
        name = args['name']
        surname = args['surname']

        user = self.user_service.create_user(name=name, surname=surname)
        resp.body = json.dumps(user.to_dict())

    @use_args(user_id_validation)
    def on_delete(self, req, resp, args):
        self.user_service.delete_user(args['user_id'])
        resp.body = json.dumps({'success': True})

