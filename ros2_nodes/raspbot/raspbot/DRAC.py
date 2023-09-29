import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32MultiArray
import smbus
import math

class DRAC(Node):
  def __init__(self):
    super().__init__('DRAC')
    self.publisher = self.create_publisher(Float32MultiArray, '/motor_control', 10)
    timer_period = 0.1
    self.timer = self.create_timer(timer_period, self.drac_callback)
    self.stop = False
    self.turn_right = [0,90] #this needs to be tweaked
    self.go_straight = [.3,0] 

    self.isTurning = False
    self.elapsed_time  = 0.0
    self.straight_duration  = 2.0
    self.turn_duration = 1 # this needs to be tweaked
    self.turn_count = 0
  
  def drac_callback(self):
    msg = Float32MultiArray()
    self.elapsed_time += 0.1

    if self.stop or self.turn_count >= 4:
        msg.data = [0,0]
        self.stop = True
        self.publisher.publish(msg)
        return
    
    msg.data = self.motor_data()
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
    return self.turn_right
  
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