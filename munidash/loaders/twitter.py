from typing import List, Any, Iterator

import requests
import xml.etree.ElementTree as ET

import twitter

from munidash.vehicle import Vehicle
from munidash.vehicle_cache import VehicleCache
from munidash.config import MUNI_METRO_ROUTES, TWITTER_API_KEY, TWITTER_SECRET_KEY, TWITTER_ACCESS_TOKEN, \
    TWITTER_ACCESS_TOKEN_SECRET


def fetch_twitter_data() -> str:
    api = twitter.Api(consumer_key=TWITTER_API_KEY,
                      consumer_secret=TWITTER_SECRET_KEY,
                      access_token_key=TWITTER_ACCESS_TOKEN,
                      access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

    return api.GetUserTimeline(screen_name='sfmta_muni')


def filter_nextbus_data(vehicle: ET.Element) -> bool:
    # TODO add whether trains are 1 or 2 car
    if all([
        vehicle.attrib.get('routeTag') in MUNI_METRO_ROUTES,
        vehicle.attrib.get('leadingVehicleId', None) is None,
    ]):
        return True
    else:
        return False


def parse_nextbus_data(nextbus_data: str) -> Iterator[Vehicle]:
    vehicles_elements = ET.fromstring(nextbus_data)
    muni_metro_elements = filter(filter_nextbus_data, vehicles_elements)
    vehicles = map(Vehicle.from_nextbus_response, muni_metro_elements)
    return vehicles


def main():
   print(fetch_twitter_data())


if __name__ == "__main__":
    main()

