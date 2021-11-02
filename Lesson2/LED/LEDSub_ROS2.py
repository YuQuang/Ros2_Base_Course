# coding=UTF-8 
import rclpy 
import time
import RPi.GPIO as GPIO
from rclpy.node import Node 
from std_msgs.msg import String 

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

class LED_sub(Node): 
    def __init__(self): 
        super().__init__('LED') 
        self.subscription = self.create_subscription(String,"chatter",self.listener_callback,10) 
        self.subscription #prevent unused variable warning 

    def listener_callback(self, msg): 
        if msg.data == 'pressed':
            GPIO.output(17,1)
            time.sleep(1)
            GPIO.output(17,0)

if __name__ == '__main__': 
    rclpy.init() 
    LED = LED_sub() 
    rclpy.spin(LED) 
    LED.destroy_node() 
    rclpy.shutdown()
