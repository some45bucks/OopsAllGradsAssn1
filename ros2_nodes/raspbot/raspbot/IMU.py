import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32MultiArray
import smbus
import time
import math


class IMU(Node):
  def __init__(self):
    super().__init__('IMU')
    self.IMU_subscription = self.create_subscription(Float32MultiArray, '/motor_control', self.IMU_callback, 10)
    self.IMU_publisher = self.create_publisher(Float32MultiArray, '/log', 10)
    self.timer_period = 0.1
    self.V = 0
    self.AV = 0
    self.startTime = time.time()
    self.time = 0
    self.timer = self.create_timer(self.timer_period, self.IMU_send)

  def IMU_send(self):
    msg = Float32MultiArray()
    msg.data = [self.V,self.AV,time.time()-self.startTime] #add time stamp for data vis
    self.IMU_publisher.publish(msg)
      
  def IMU_callback(self, msg):
    self.V = msg.data[0]
    self.AV = msg.data[1]



def main(args=None):
  rclpy.init(args=args)
  
  imu = IMU()
  
  try:
    rclpy.spin(imu)
  except KeyboardInterrupt as e:
    print(e)
  except Exception as e:
    print(e)
  
  imu.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()