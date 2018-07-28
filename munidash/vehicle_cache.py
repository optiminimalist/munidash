import pickle
from typing import List

import redis

from munidash.config import MUNI_METRO_ROUTES
from munidash.vehicle import Vehicle


class VehicleCache:
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def update_vehicles(self, list_of_vehicles: List[Vehicle]):
        for route_tag in MUNI_METRO_ROUTES:
            if self.r.llen(route_tag) > 0:
                print(f"Deleting {route_tag}")
                self.r.delete(route_tag)

        for vehicle in list_of_vehicles:
            self.r.lpush(vehicle.route_tag, pickle.dumps(vehicle))

    def get_vehicles_by_route_tag(self, route_tag: str) -> List[Vehicle]:
        pickled_vehicles = self.r.lrange(route_tag, 0, self.r.llen(route_tag))

        return map(pickle.loads, pickled_vehicles)