import redis
from config.settings.local import REDIS_CONFIG

redis_client = redis.StrictRedis(
    host=REDIS_CONFIG['HOST'],
    port=REDIS_CONFIG['PORT'],
    password=REDIS_CONFIG['PASSWORD'],
    decode_responses=True,
    socket_connect_timeout=3
)


def set_redis_val(key, value, ttl=None, only_if_not_exists=False, if_exists=False, ack=False):
    ret = redis_client.set(key, value, ttl, nx=only_if_not_exists, xx=if_exists)
    if ack:
        return ret


def get_redis_val(key):
    return redis_client.get(key)


def is_redis_val_exists(key):
    return redis_client.exists(key)


def delete_redis_val(key):
    return redis_client.delete(key)


def get_redis_ttl(key):
    return redis_client.ttl(key)


def set_redis_hash_map(dict_name, dict_to_set, ack=False):
    ret = redis_client.hmset(dict_name, dict_to_set)
    if ack:
        return ret


def get_redis_hash_map(dict_name, keys):
    return redis_client.hmget(dict_name, keys)


def get_redis_hash_all_keys(dict_name):
    return redis_client.hkeys(dict_name)


def get_redis_hash_all_vals(dict_name):
    return redis_client.hkeys(dict_name)


def is_redis_hmap_exists(dict_name, key):
    return redis_client.hexists(dict_name, key)


def get_redis_client():
    return redis_client


def push_left_redis(key, values=[]):
    return redis_client.lpush(key, values)


def push_right_redis(key, values=[]):
    return redis_client.rpush(key, values)


def pop_left_redis(key):
    return redis_client.lpop(key)


def pop_right_redis(key):
    return redis_client.rpop(key)


def get_list_range_redis(key, start_index, end_index):
    return redis_client.lrange(key, start_index, end_index)


def get_all_list_redis(dict_name):
    return redis_client.hgetall(dict_name)


def set_expire_list_redis(dict_name,ttl,ack =False):
    ret = redis_client.expire(dict_name,ttl)
    if ack:
        return ret


def get_redis_list_length(key):
    return redis_client.llen(key)


def remove_element_from_redis_list(key, count, value):
    return redis_client.lrem(key, count, value)
