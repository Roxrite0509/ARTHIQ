import redis
from config import REDIS_URL

redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)


def set_session(key: str, value: str, ttl: int = 3600):
    redis_client.setex(key, ttl, value)


def get_session(key: str):
    return redis_client.get(key)
