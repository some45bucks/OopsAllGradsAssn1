import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray
import smbus
import time
import math
from time import sleep
class MinimalPublisher(Node):
  def __init__(self):
    super().__init__('motorsPublish')
    self.publisher = self.create_publisher(Int32MultiArray, '/motor_control', 10)
    timer_period = 0.1 # seconds between scans
    self.timer = self.create_timer(timer_period, self.motor_callback)
    self.stop = False
  
  def motor_callback(self):
    if self.stop:
      return
    msg = Int32MultiArray()
    msg.data = [75,-75]
    self.publisher.publish(msg)
    sleep(2)
    msg.data = [0,0]
    self.publisher.publish(msg)
    self.stop = True




def main(args=None):
  rclpy.init(args=args)
  
  publisher = MinimalPublisher()
  try:
    rclpy.spin(publisher)
  except KeyboardInterrupt as e:
    print(e)
  except Exception as e:
    print(e)
  
  publisher.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()