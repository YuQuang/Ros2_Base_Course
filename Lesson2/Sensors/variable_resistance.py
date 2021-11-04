import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

while True:
    d = GPIO.input(17)
    print(d)
    time.sleep(0.01)

