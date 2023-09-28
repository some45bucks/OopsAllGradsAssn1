import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray
import smbus
import math

class DRAC(Node):
  def __init__(self):
    super().__init__('DRAC')
    self.publisher = self.create_publisher(Int32MultiArray, '/motor_control', 10)
    timer_period = 0.1
    self.timer = self.create_timer(timer_period, self.drac_callback)
    self.stop = False
    self.turn_left = [0,-1]
    self.go_straight = [1,0]

    self.isTurning = False
    self.elapsed_time  = 0.0
    self.straight_duration  = 2.0
    self.turn_duration = 1
    self.turn_count = 0
    print('drac')
  
  def drac_callback(self):
    if self.stop or self.turn_count >= 3:
      return
    
    msg = Int32MultiArray()
    msg.data = self.motor_data()
    self.elapsed_time += 0.1
    self.publisher.publish(msg)    
    
  def motor_data(self):
    if self.isTurning:
      return self.turn_left_data()
    else:
      return self.go_straight_data()
    
  # turn -> straight or continue turning
  def turn_left_data(self):
    if self.elapsed_time >= self.turn_duration:
      self.isTurning = False
      self.elapsed_time = 0.0
    return self.turn_left
  
  # straight -> turn or continue straight
  def go_straight_data(self):
    if self.elapsed_time >= self.straight_duration:
      self.turn_count += 1
      self.isTurning = True
      self.elapsed_time = 0.0
    return self.go_straight



def main(args=None):
  rclpy.init(args=args)
  
  publisher = DRAC()
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