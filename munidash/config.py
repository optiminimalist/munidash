import os
import urllib

REDIS_URL = urllib.parse.urlparse(os.environ.get('REDISCLOUD_URL'))
print(REDIS_URL)

MUNI_METRO_ROUTES = frozenset(["N", "M", "L", "KT", "J", "C", "S"])