import serial
from time import sleep

ser = serial.Serial("/dev/ttyACM0", 115200, timeout=0.5)

try:
    ser.write(b"back\n")
    ser.write(b"forward\n")
    sleep(5)
except KeyboardInterrupt as e:
    print(f"{e}")
finally:
    ser.write(b"stop\n")
    ser.close()