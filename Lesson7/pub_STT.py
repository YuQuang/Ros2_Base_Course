# coding=UTF-8 
import rclpy 
import time
from rclpy.node import Node 
from std_msgs.msg import String
import speech_recognition as sr


class STT_pub(Node): 
    def __init__(self): 
        super().__init__('STT')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        r = sr.Recognizer()
        source = sr.Microphone()
        fromLanguage = "zh-TW"
        toLanguage = "en"

    def run(self):
        while 1:
            if input("Q to quit, Enter to continue") == 'q':break
            print("Say something...")
            audio = self.r.listen(self.source)
            sttTXT_org = self.r.recognize_google(audio, language = self.fromLanguage)
            msg = String() 
            msg.data = sttTXT_org
            if msg.data != None:self.publisher_.publish(msg) 

if __name__ == '__main__': 
    rclpy.init() 
    SoundToText = STT_pub() 
    SoundToText.run()
    SoundToText.destroy_node() 
    rclpy.shutdown()
