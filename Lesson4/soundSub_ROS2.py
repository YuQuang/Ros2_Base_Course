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
        mixer.init()
        if msg.data == 'morning':
            mixer.music.load('morning.mp3')
        if msg.data == 'night':        
            mixer.music.load('night.mp3')
        try:
            mixer.music.play()
            while mixer.music.get_busy() == True:continue
        except:pass
        
if __name__ == '__main__': 
    rclpy.init() 
    Sound = Sound_sub() 
    rclpy.spin(Sound) 
    Sound.destroy_node() 
    rclpy.shutdown()
