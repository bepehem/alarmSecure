import RPi.GPIO as GPIO
import time
from threading import Thread

class Buzzer:
    def __init__(self, numGPIO):
        self.numGPIO = numGPIO
        GPIO.setup(numGPIO, GPIO.OUT)

    def on(self):
        print('Buzzer {} on'.format(self.numGPIO))
        GPIO.output(self.numGPIO, GPIO.HIGH)

    def off(self):
        print('Buzzer {} off'.format(self.numGPIO))
        GPIO.output(self.numGPIO, GPIO.LOW)


