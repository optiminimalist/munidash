from operator import attrgetter

from flask import Flask, jsonify, render_template

from munidash.vehicle_cache import VehicleCache

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
        [
            vehicle._asdict()
            for vehicle in vehicle_cache.get_all_vehicles()
        ]
    )


if __name__ == '__main__':
    app.run()
