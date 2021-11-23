# coding=UTF-8 
import rclpy 
import time
import RPi.GPIO as GPIO
from rclpy.node import Node 
from std_msgs.msg import String 

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)

class button_pub(Node): 
    def __init__(self): 
        super().__init__('button')
        # 定義節點包含一個發送端 
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
 
    def run(self): 
        msg = String() 
        # 由於是物件導向，訊息也是字串物件裡面的一個屬性
        msg.data = 'pressed'
        # 呼叫發送端發送訊息
        count = 0
        while 1:
            if GPIO.input(18) == 0:
                msg = String() 
                if count%2 == 0:msg.data = 'food'#新增判斷
                else: msg.data = 'nofood'
                self.publisher_.publish(msg) 
                count += 1
                time.sleep(1) #新增這行


if __name__ == '__main__': 
    rclpy.init()
    button = button_pub() 
    button.run()
    button.destroy_node() 
    rclpy.shutdown()
