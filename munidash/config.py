import os
import urllib

REDIS_URL = urllib.parse.urlparse(os.environ.get('REDISCLOUD_URL', "redis://localhost:6379/"))
TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')
TWITTER_SECRET_KEY = os.environ.get('TWITTER_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

MUNI_METRO_ROUTES = frozenset(["N", "M", "L", "KT", "J", "S", "MBUS"])