# coding=UTF-8 
import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String
from gtts import gTTS
import os 

class playrobot_TTS(Node):
    """基本文字轉語音節點
       訂閱：chatter型別字串
       發布：無"""
    def __init__(self): 
        super().__init__('playrobot_TTS')
        self.subscription = self.create_subscription(String,"chatter",self.TTS_callback,10) 
        self.subscription #prevent unused variable warning

    def TTS_callback(self, msg):
        print(msg.data)
        output = gTTS(text=msg.data, lang="zh-tw", slow=False)
        output.save("output.mp3")
        # Play the converted file 
        os.system("start output.mp3")

if __name__ == '__main__': 
    rclpy.init()
    node_TTS = playrobot_TTS()
    rclpy.spin(node_TTS) 
    node_TTS.destroy_node() 
    rclpy.shutdown()