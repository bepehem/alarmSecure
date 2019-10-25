import RPi.GPIO as GPIO
import time
from threading import Thread

class Led:
    def __init__(self, numGPIO):
        self.numGPIO = numGPIO
        GPIO.setup(numGPIO, GPIO.OUT)

    def on(self):
        GPIO.output(self.numGPIO, GPIO.HIGH)

    def off(self):
        GPIO.output(self.numGPIO, GPIO.LOW)

    def blink(self, numBlink, sleepTime):
        i = 0
        while i < numBlink:
            self.on()
            time.sleep(sleepTime)
            self.off()
            time.sleep(sleepTime)
            i += 1

    def asyncBlink(self, numBlink, sleepTime):
        thread = Thread(target=self.blink, args=(numBlink, sleepTime, ))
        thread.start()
        return thread


