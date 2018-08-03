from operator import attrgetter

from flask import Flask, jsonify, render_template

from munidash.vehicle_cache import VehicleCache
import datetime

app = Flask(__name__)


@app.route('/')
def main():
    vehicle_cache = VehicleCache()

    return render_template("main.html")
    # return jsonify({
    #     'last_updated_time': vehicle_cache.get_last_updated_time(),
    #     'vehicles': list(map(lambda x: attrgetter("vehicle_id"), vehicle_cache.get_all_vehicles()))
    # })

@app.route('/all_vehicles.json')
def get_all_vehicles():
    vehicle_cache = VehicleCache()

    return jsonify(
    {
        "vehicles": [
            vehicle._asdict()
            for vehicle in vehicle_cache.get_vehicles_by_route_tag('N')
        ],
        "last_updated_time": datetime.datetime.utcfromtimestamp(float(vehicle_cache.get_last_updated_time()))
    }

    )


if __name__ == '__main__':
    app.run()
