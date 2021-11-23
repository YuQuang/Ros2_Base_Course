# coding=UTF-8 
import rclpy 
import time
import epd2in9
from PIL import Image,ImageDraw,ImageFont
from rclpy.node import Node 
from std_msgs.msg import String 

epd = epd2in9.EPD()
epd.init(epd.lut_full_update)

class ePaper_sub(Node): 
    def __init__(self): 
        super().__init__('ePaper') 
        self.subscription = self.create_subscription(String,"chatter",self.listener_callback,10) 
        self.subscription #prevent unused variable warning 

    def listener_callback(self, msg): 
        if msg.data == 'pressed':
            image = Image.open('food.bmp')
            epd.set_frame_memory(image, 0, 0)
            epd.display_frame()

if __name__ == '__main__': 
    rclpy.init() 
    ePaper = ePaper_sub() 
    rclpy.spin(ePaper) 
    ePaper.destroy_node() 
    rclpy.shutdown()
