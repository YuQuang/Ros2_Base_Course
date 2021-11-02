import RPi.GPIO as GPIO
import time

# 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.IN)

while True:
    value01 = GPIO.input(18)
    GPIO.output(17, 1 - value01 )
    time.sleep(0.1)
