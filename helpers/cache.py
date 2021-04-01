import redis
import json\


redis_client = redis.Redis('localhost')


class Cache:

    @classmethod
    def set(cls, key, value, time=86400):
        redis_client.set(str(key), value, ex=time)

    @classmethod
    def get(cls, key):
        value = redis_client.get(key)
        return value

    @classmethod
    def hmset(cls, key, dict_value):
        byte_dict_value = json.dumps(dict_value)
        redis_client.hmset(name=key, mapping=dict_value)

    @classmethod
    def hgetall(cls, key):
        value = redis_client.hgetall(key)
        return value

    pass
