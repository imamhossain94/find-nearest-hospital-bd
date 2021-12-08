import os
import sys
import json
import time
from flask import Flask, request, jsonify

sys.path.insert(0, os.getcwd() + '/apis')

app = Flask(__name__)


def dist_between_two_lat_lon(*args):
    from math import asin, cos, radians, sin, sqrt
    lat1, lat2, long1, long2 = map(radians, args)

    dist_lats = abs(lat2 - lat1)
    dist_longs = abs(long2 - long1)
    a = sin(dist_lats / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dist_longs / 2) ** 2
    c = asin(sqrt(a)) * 2
    radius_earth = 6378  # the "Earth radius" R varies from 6356.752 km at the poles to 6378.137 km at the equator.
    return c * radius_earth


def find_closest_lat_lon(data, v):
    try:
        return min(data, key=lambda p: dist_between_two_lat_lon(v['lat'], p['lat'], v['lon'], p['lon']))
    except TypeError:
        print('Not a list or not a number.')


@app.route('/')
def welcome():
    return '<h1 align="center">Successfully Running</h1>'


# Main route
@app.route('/main/v1/loc', methods=['GET'])
def data_url():
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    if lat is not None and lng is not None:
        f = open('hospitals.json')
        city_list = json.load(f)
        city_to_find = {'lat': float(lat), 'lon': float(lng)}
        data = {
            'status': 'success',
            'data': find_closest_lat_lon(city_list, city_to_find),
            'timestamp': time.time()
        }
    else:
        data = {'status': 'failed', 'reason': 'No URL Provided!'}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
