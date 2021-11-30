# coding=UTF-8 
import rclpy 
import serial
from rclpy.node import Node 
from std_msgs.msg import String 

class Motor_sub(Node): 
    def __init__(self): 
        super().__init__('Motor')
        self.port = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)
        self.controlCmd = {'front':'1_50\n', 'left':'3_50\n', 'right':'2_50\n', 'back':'4_50\n'}
        self.subscription = self.create_subscription(String,"chatter",self.listener_callback,10) 
        self.subscription

    def listener_callback(self, msg): 
        print(msg.data)
        if msg.data in self.controlCmd:    
            self.port.write(self.controlCmd[msg.data].encode())

if __name__ == '__main__': 
    rclpy.init() 
    Motor = Motor_sub() 
    rclpy.spin(Motor) 
    Motor.destroy_node() 
    rclpy.shutdown()
