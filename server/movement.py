import RPi.GPIO as GPIO
from led import Led
from GPIO import GPIO_initialize
import time
from threading import Thread

class Movement:

    def __init__(self, numGPIO, detectFunction = None, readyFunction = None):
        self.numGPIO = numGPIO
        GPIO.setup(self.numGPIO, GPIO.IN)
        self.running = False
        self.detectFunction = detectFunction
        self.readyFunction = readyFunction

    def detect(self):
        currentstate = 0
        previousstate = 0
        while self.running:
            currentstate = GPIO.input(self.numGPIO)
            if currentstate == 1 and previousstate == 0:
                if not (self.detectFunction is None):
                    self.detectFunction()
                previousstate = 1
            elif currentstate == 0 and previousstate == 1:
                if not (self.readyFunction is None):
                    self.readyFunction()
                previousstate = 0
            time.sleep(0.01)

    def startDetection(self):
        self.running = True
        thread = Thread(target=self.detect)
        thread.start()
        return thread

    def stopDetection(self):
        self.running = False

GPIO_initialize()
led = Led(24)

def detectMovement():
    led.asyncBlink(5, 0.10)

movementSensor = Movement(17, detectFunction=detectMovement)
thread = movementSensor.startDetection()



