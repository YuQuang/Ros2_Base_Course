import rclpy #import rclpy模組 
import time
from rclpy.node import Node 

class Ex_2(Node): 
    def __init__(self): 
        super().__init__('Ex_2') #初始化  
        #計時執行timer_callback
        self.timer = self.create_timer(1, self.timer_callback) 
       
    def timer_callback(self): 
        #印出 Hello World
        self.get_logger().info('[' + str(time.time()) + ']Hello World')
    
if __name__ == '__main__': 
    rclpy.init() 
    ex2 = Ex_2() 
    rclpy.spin(ex2)    #讓ex2節點保持執行
    ex2.destroy_node() 
    rclpy.shutdown()

