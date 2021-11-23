# coding=UTF-8 
import rclpy 
import time
from pygame import mixer
from rclpy.node import Node 
from std_msgs.msg import String 

class Sound_sub(Node): 
    def __init__(self): 
        super().__init__('Sound') 
        self.subscription = self.create_subscription(String,"chatter",self.listener_callback,10) 
        self.subscription

    def listener_callback(self, msg): 
        if msg.data == 'pressed':
            mixer.init()
            mixer.music.load('test.mp3')
            mixer.music.play()
            while mixer.music.get_busy() == True:continue
            mixer.music.stop()
            mixer.quit()

if __name__ == '__main__': 
    rclpy.init() 
    Sound = Sound_sub() 
    rclpy.spin(Sound) 
    Sound.destroy_node() 
    rclpy.shutdown()
