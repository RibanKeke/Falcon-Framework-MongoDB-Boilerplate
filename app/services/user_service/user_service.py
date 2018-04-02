"""
Author: Robert Banziziki
Date: 23 february 2018
"""

from app.models.user import User


class UserService(object):
    """
    Service for creating a new app project
    """
    @staticmethod
    def create_user(name, surname):
        """
        Create a new user
        """
        user = User(name=name, surname=surname).save()
        return user

    @staticmethod
    def list_users():
        """
        Get created projects
        :return:
        :rtype:
        """
        return User.objects()

    @staticmethod
    def delete_user(user_id):
        """
        Delete the user
        """
        User.objects(id=user_id).delete()

