import json
from datetime import timedelta

from redis import Redis


class RedisDBConnector(object):
    """encapsulates redis database backend functions"""

    def __init__(self, host, port, password):
        self.redisdb_client = Redis(
            host=host,
            port=port,
            password=password,
            db=0
        )

    def add_product(self, product_id, product_details):
        """
        add key-value pair to redis database

        :params data: dict of key-value pairs to be added
        :return True
        """
        self.redisdb_client.setex(product_id, timedelta(minutes=5), json.dumps(product_details, default=str))

        return True

    def get_product_by_id(self, product_id):
        """
        get key value from redis database

        :params keys: list of keys
        :return rtype -> dict, values from redis database
        """
        product_details = self.redisdb_client.get(product_id)

        if isinstance(product_details, str) or isinstance(product_details, bytes):
            product_details = json.loads(product_details)

        return product_details

    def remove(self, keys):
        """
        delete key-value pair from redis database

        :params keys: list of keys
        :return None
        """
        if not isinstance(keys, list):
            raise Exception("expected list of keys")

        for k in keys:
            print(self.redisdb_client.delete(k))

        return True

