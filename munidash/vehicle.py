from collections import namedtuple
from enum import Enum

VehicleTuple = namedtuple("Vehicle", "lat lon route_tag vehicle_id direction_tag secs_since_report heading speed")

class VehicleDirection(Enum):
    INBOUND = 1
    OUTBOUND = 2

class UnknownVehicleDirectionException(Exception):
    pass

class Vehicle(VehicleTuple):
    @staticmethod
    def from_nextbus_response(v):
        return Vehicle(
            v.attrib['lat'], v.attrib['lon'], v.attrib.get('routeTag'), v.attrib['id'], v.attrib.get('dirTag'),
            v.attrib.get('secsSinceReport'), v.attrib.get('heading'), v.attrib.get('speedKmHr')
        )

    @property
    def direction(self) -> VehicleDirection:
        if "I" in self.direction_tag:
            return VehicleDirection.INBOUND
        if "O" in self.direction_tag:
            return VehicleDirection.OUTBOUND

        raise UnknownVehicleDirectionException()