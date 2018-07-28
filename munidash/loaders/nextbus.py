from typing import List, Any, Iterator

import requests
import xml.etree.ElementTree as ET

from munidash.vehicle import Vehicle
from munidash.vehicle_cache import VehicleCache
from munidash.config import MUNI_METRO_ROUTES

def fetch_nextbus_data() -> str:
    return requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=vehicleLocations&a=sf-muni&t=0").text


def parse_nextbus_data(nextbus_data: str) -> Iterator[Vehicle]:
    vehicles_elements = ET.fromstring(nextbus_data)
    muni_metro_elements = [
        vehicle
        for vehicle in vehicles_elements
        if vehicle.attrib.get('routeTag') in MUNI_METRO_ROUTES
    ]
    vehicles = map(Vehicle.from_nextbus_response, muni_metro_elements)
    return vehicles


def main():
    # fetch data from nextbus
    nextbus_data = fetch_nextbus_data()
    vehicles = parse_nextbus_data(nextbus_data)

    vehicle_cache = VehicleCache()
    vehicle_cache.update_vehicles(vehicles)

    print(next(vehicle_cache.get_vehicles_by_route_tag("N")))


if __name__ == "__main__":
    main()