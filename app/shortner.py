import redis
import os
import secrets

APP_BASE_URL = os.getenv('APP_BASE_URL', default="http://localhost:5000")
redis_url = os.getenv('REDIS_URL', default="redis://localhost:6379")
redis_server = redis.Redis.from_url(redis_url)
expiration_time = int(os.getenv("EXPIRATION_TIME", default=604800)) #Default to 7 days

def shorten(url: str) -> str:
    short_url = secrets.token_urlsafe(6)
    redis_server.set(short_url, url, ex=expiration_time)
    return f"{APP_BASE_URL}/{short_url}"

def get_url(short_url: str) -> str:
    url = redis_server.get(short_url)
    if url is None:
        raise ValueError("Not found")
    return url.decode('utf-8')