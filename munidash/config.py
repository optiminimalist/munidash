import os
import urllib

REDIS_URL = urllib.parse.urlparse(os.environ.get('REDISCLOUD_URL', "redis://localhost:6379/"))

MUNI_METRO_ROUTES = frozenset(["N", "M", "L", "KT", "J", "C", "S", "MBUS"])