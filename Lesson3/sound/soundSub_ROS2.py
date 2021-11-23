# coding=UTF-8 
import rclpy 
import time
import threading
from pygame import mixer
from rclpy.node import Node 
from std_msgs.msg import String 

class Sound_sub(Node): 
    def __init__(self): 
        super().__init__('Sound') 
        self.subscription = self.create_subscription(String,"chatter",self.listener_callback,10) 
        self.subscription
        self.skip = False

    def listener_callback(self, msg): 
        if msg.data == 'pressed':
            print('skip')
            self.skip = True

    def music(self):
        musicList = ['1.mp3', '2.mp3', '3.mp3']
        musicIndex = 0
        while 1:
            mixer.init()
            while mixer.music.get_busy() == True:continue
            if self.skip:
                mixer.music.stop()
                mixer.music.load(musicList[musicIndex])
                mixer.music.play()
                musicIndex += 2
                musicIndex %= 3
                self.skip = False
                time.sleep(1)
            else:
                mixer.music.stop()
                mixer.music.load(musicList[musicIndex])
                mixer.music.play()
                musicIndex += 1
                musicIndex %= 3
                time.sleep(1)
        mixer.quit()

if __name__ == '__main__': 
    rclpy.init() 
    Sound = Sound_sub() 
    t = threading.Thread(target = Sound.music)
    t.setDaemon(True)
    t.start()
    rclpy.spin(Sound) 
    Sound.destroy_node() 
    rclpy.shutdown()
