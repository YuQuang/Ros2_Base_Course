import rclpy #import rclpy模組 
import time
from rclpy.node import Node 

class Ex_2(Node): 
    def __init__(self): 
        super().__init__('Ex_2') #初始化  
       
    def timer_callback(self): 
        while 1:
            self.get_logger().info('[' + str(time.time()) + ']Hello World')
            time.sleep(1)

if __name__ == '__main__': 
    rclpy.init() 
    ex2 = Ex_2() 
    ex2.timer_callback()
    ex2.destroy_node() 
    rclpy.shutdown()