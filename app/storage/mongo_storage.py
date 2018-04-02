"""
Author: Robert Banziziki
Date: 22 february 2018
"""

import builtins
import logging

import mongoengine as mongo

LOG = logging.getLogger(__name__)
MODELS = []


class MongoStorage(object):
    """
    Proxy object for models defined in mongo_db
    """

    def __init__(self, db_name, mongo_uri):
        # Disconnect any pending default connection
        mongo.connection.disconnect('default')
        self.db = mongo.connect(db=db_name, host=mongo_uri)
        LOG.info("Connected to mongo db_database: {}".format(mongo_uri))
