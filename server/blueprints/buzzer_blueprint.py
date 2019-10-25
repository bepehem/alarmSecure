from flask import Blueprint, redirect, url_for
from buzzer import Buzzer
from GPIO import GPIO_initialize

bp_buzzer = Blueprint('buzzer', __name__, url_prefix='/buzzer')

GPIO_initialize()

buzz = Buzzer(22)

@bp_buzzer.route('/on/<buzzer_name>')
def buzzer_on(buzzer_name):
    buzz.on()
    return redirect(url_for('index'))

@bp_buzzer.route('/off/<buzzer_name>')
def buzzer_off(buzzer_name):
    buzz.off()
    return redirect(url_for('index'))
