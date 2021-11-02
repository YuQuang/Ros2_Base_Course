import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

LEDon = GPIO.output(17, 1)
time.sleep(1)
LEDoff = GPIO.output(17, 0)

