import rclpy #import rclpy模組 
from rclpy.node import Node

class Ex_hello(Node): 
    def __init__(self): 
        super().__init__('Ex_hello') #初始化 hello_python_node 
        self.get_logger().info('Hello World') #印出 Hello World 
        
if __name__ == '__main__': 
    rclpy.init() 
    ex1 = Ex_hello() 
    ex1.destroy_node() #用完記得把node清除
    rclpy.shutdown()
