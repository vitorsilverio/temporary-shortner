import redis
import os
from dotenv import load_dotenv
import secrets

load_dotenv()
APP_BASE_URL = os.getenv('APP_BASE_URL', default="http://localhost:5000")

def shorten(url: str) -> str:
    redis_url = os.getenv('REDIS_URL', default="redis://localhost:6379")
    r = redis.Redis.from_url(redis_url)
    short_url = secrets.token_urlsafe(6)
    r.set(short_url, url, ex=int(os.getenv("EXPIRATION_TIME", default=604800))) #Default to 7 days
    return f"{APP_BASE_URL}/{short_url}"

def get_url(short_url: str) -> str:
    redis_url = os.getenv('REDIS_URL', default="redis://localhost:6379")
    r = redis.Redis.from_url(redis_url)
    url = r.get(short_url)
    if url is None:
        raise ValueError("Invalid short URL")
    return url.decode('utf-8')