import json

import redis


class Storage:
    def __init__(self, redis_url: str):
        host, port = redis_url.split(":")
        self._redis = redis.Redis(host=host, port=port, db=0)
        self._key = "dummy-data"

    @property
    def dummies(self):
        return json.loads(self._redis.get(self._key))

    @dummies.setter
    def dummies(self, value):
        self._redis.set(self._key, json.dumps(value))
