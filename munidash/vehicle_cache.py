import itertools
import pickle
import time
from typing import List, Iterator

import redis

from munidash.config import MUNI_METRO_ROUTES, REDIS_URL
from munidash.vehicle import Vehicle


class VehicleCache:
    def __init__(self):
        self.r = redis.Redis(host=REDIS_URL.hostname, port=REDIS_URL.port, password=REDIS_URL.password)

    def update_vehicles(self, list_of_vehicles: Iterator[Vehicle]):
        for route_tag in MUNI_METRO_ROUTES:
            if self.r.llen(route_tag) > 0:
                print(f"Deleting {route_tag}")
                self.r.delete(route_tag)

        for vehicle in list_of_vehicles:
            self.r.lpush(vehicle.route_tag, pickle.dumps(vehicle))

        self.r.set("last_updated_time", time.time())

    def get_vehicles_by_route_tag(self, route_tag: str) -> Iterator[Vehicle]:
        pickled_vehicles = self.r.lrange(route_tag, 0, self.r.llen(route_tag))

        return map(pickle.loads, pickled_vehicles)

    def get_all_vehicles(self) -> Iterator[Vehicle]:

        return map(pickle.loads, itertools.chain(
            *[
                self.r.lrange(route_tag, 0, self.r.llen(route_tag))
                for route_tag in MUNI_METRO_ROUTES
            ]
        ))


    def get_last_updated_time(self):
        return self.r.get("last_updated_time")

