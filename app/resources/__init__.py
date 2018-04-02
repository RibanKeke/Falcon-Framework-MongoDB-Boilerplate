"""
Author:
Date:
"""
from .users import UserResources

def configure_routes(app):
    """
    Configure all available routes on the app
    :param app: The falcon app instance
    :type app: falcon.API
    """
    app.add_route("/users", UserResources())