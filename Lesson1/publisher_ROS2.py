# coding=UTF-8 
import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String 
class Ex3_pub(Node): 
    def __init__(self): 
        super().__init__('Ex3_pub')
        # 定義節點包含一個發送端 
        self.publisher_ = self.create_publisher(String, 'chatter', 10) 
        self.timer = self.create_timer(1, self.timer_callback) 
    def timer_callback(self): 
        msg = String() 
        # 由於是物件導向，訊息也是字串物件裡面的一個屬性
        msg.data = 'Hello World'
        # 呼叫發送端發送訊息
        self.publisher_.publish(msg) 

if __name__ == '__main__': 
    rclpy.init() 
    ex3_publisher = Ex3_pub() 
    rclpy.spin(ex3_publisher) 
    ex3_publisher.destroy_node() 
    rclpy.shutdown()
