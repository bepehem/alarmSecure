# export FLASK_APP=application.py
# flask run --host=0.0.0.0
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from threading import Thread


app = Flask(__name__)
socketio = SocketIO(app)

from blueprints.led_blueprint import bp_led
from blueprints.buzzer_blueprint import bp_buzzer
from movement import Movement


app.register_blueprint(bp_led)
app.register_blueprint(bp_buzzer)

@app.route('/')
def index():
    return render_template('index.html', detectFunction=movementDetected)


def movementDetected():
    socketio.emit('alert', 'Mouvement détecté', Broadcast=True)


def message_loop():
    while True:
        message = input('Votre message ?')
        socketio.emit('alert', message, Broadcast=True)

# # Vue que notre méthode pour lire nos message est une boucle infinie
# # Elle bloquerait notre serveur. Qui ne pourrait répondre à aucune requête.
# # Ici nous créons un Thread qui va permettre à notre fonction de se lancer
# # en parallèle du serveur.
# read_messages = Thread(target=message_loop)
# read_messages.start()
