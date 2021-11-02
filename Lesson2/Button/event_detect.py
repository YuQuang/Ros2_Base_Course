import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pinStatus = 1
def buttonPressed(channel):
    global pinStatus
    pinStatus = abs(pinStatus - 1)
    GPIO.output(17, pinStatus)

GPIO.add_event_detect(18, GPIO.RISING, callback=buttonPressed, bouncetime=100)

while True:
    time.sleep(1)
    print(f"Status now : { pinStatus }")

GPIO.remove_event_detect(18)
GPIO.cleanup()