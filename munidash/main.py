from flask import Flask

from munidash.vehicle_cache import VehicleCache

app = Flask(__name__)


@app.route('/')
def main():
    vehicle_cache = VehicleCache()

    return vehicle_cache.get_last_updated_time() #next(vehicle_cache.get_vehicles_by_route_tag("N")).route_tag


if __name__ == '__main__':
    app.run()
