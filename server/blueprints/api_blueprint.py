from flask import Blueprint, redirect, url_for, jsonify
from movement import Movement
from led import Led
from GPIO import GPIO_initialize

bp_api = Blueprint('api', __name__, url_prefix='/api/')

motion = Movement(17)

GPIO_initialize()

leds = {
    'led': Led(24)
}



# @bp_api.route('/move')
# def move_json():
#     move= movementSensor.startDetection()
#     return jsonify({
#         'thread': movementSensor
#     })