# coding=UTF-8 
import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String 

class Ex3_sub(Node): 
    def __init__(self): 
        super().__init__('Ex3_sub') 
        self.subscription = self.create_subscription(String,"chatter",self.listener_callback,10) 
        self.subscription #prevent unused variable warning 

    def listener_callback(self, msg): 
        self.get_logger().info('I heard: "%s"' % msg.data) 

if __name__ == '__main__': 
    rclpy.init() 
    ex3_subscriber = Ex3_sub() 
    rclpy.spin(ex3_subscriber) 
    ex3_subscriber.destroy_node() 
    rclpy.shutdown()
