from flask import Blueprint, redirect, url_for
from movement import Movement
from GPIO import GPIO_initialize

bp_move = Blueprint('move', __name__, url_prefix='/move')

GPIO_initialize()

motion = Movement(17)

@bp_move.route('/on/<move_name>')
def move_on(move_name):
    motion.on()
    return redirect(url_for('index'))

@bp_move.route('/off/<move_name>')
def move_off(move_name):
    motion.off()
    return redirect(url_for('index'))