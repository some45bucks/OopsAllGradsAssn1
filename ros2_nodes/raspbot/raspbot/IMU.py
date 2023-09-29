import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray
import smbus
import time
import math


class IMU(Node):
  def __init__(self):
    super().__init__('IMU')
    self.IMU_subscription = self.create_subscription(Int32MultiArray, '/motor_control', self.IMU_callback, 10)
    self.IMU_publisher = self.create_publisher(Int32MultiArray, '/IMU', 10)
    timer_period = 0.1
    self.timer = self.create_timer(timer_period, self.IMU_send)

  def IMU_send(self):
    msg = Int32MultiArray()
    msg.data = [self.currentX,self.currentY,self.currentTheta]
    self.IMU_publisher.publish(msg)
      
  def IMU_callback(self, msg):
    V = msg.data[0]
    AV = msg.data[1]



def main(args=None):
  rclpy.init(args=args)
  
  subscriber = IMU()
  
  try:
    rclpy.spin(subscriber)
  except KeyboardInterrupt as e:
    print(e)
  except Exception as e:
    print(e)
  
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()