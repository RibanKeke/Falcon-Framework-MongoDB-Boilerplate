import logging

import falcon

from app.config import parser, settings
from app.middleware import CrossDomain
from app.resources import configure_routes
from app.util.config import setup_vyper
from app.util.error import error_handler
from app.util.logging import setup_logging
from app.storage.mongo_storage import MongoStorage

logger = logging.getLogger(__name__)


def configure(**overrides):
    logging.getLogger("vyper").setLevel(logging.WARNING)
    setup_vyper(parser, overrides)


def create_app():
    setup_logging()

    app = falcon.API(
        middleware=[
            CrossDomain()
        ],
    )

    app.add_error_handler(Exception, error_handler)

    configure_routes(app)

    return app


def start():
    logger.info("Environment: {}".format(settings.get("ENV_NAME")))
