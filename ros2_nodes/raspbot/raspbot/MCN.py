import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32MultiArray
import smbus
import time
import math

class Car:
    def __init__(self):
        self._addr = 0x16
        self._device = smbus.SMBus(1)

    def __write_u8(self, register, data):
        try:
            self._device.write_byte_data(self._addr, register, data)
        except:
            print('write_u8 error')

    def __write_register(self, register):
        try:
            self._device.write_byte(self._addr, register)
        except:
            print('write_register error')

    def __write_array(self, register, data):
        try:
            self._device.write_i2c_block_data(self._addr, register, data)
        except:
            print('write_array error')

    def control_car(self, left, right):
        """
        left: int (-255, 255)
        right: int (-255, 255)

        sets the motor with the speed given (not actually in unit, just a power amount)
        """
        register = 0x01
        left_direction = 0 if left < 0 else 1
        right_direction = 0 if right < 0 else 1

        if left < 0:
            left *= -1
        if right < 0:
            right *= -1

        data = [left_direction, left, right_direction, right]
        self.__write_array(register, data)

    def stop(self):
        register = 0x02
        self.__write_u8(register, 0x00)

    def set_servo(self, servo_id, angle):
        register = 0x03
        if angle < 0:
            angle = 0
        elif angle > 180:
            angle = 180
        data = [servo_id, angle]
        self.__write_array(register, data)


class MCN(Node):
  def __init__(self):
    super().__init__('MCN')
    self.car = Car()
    self.motor_subscription = self.create_subscription(Float32MultiArray, '/motor_control', self.motor_callback, 10)
  
  def motor_callback(self, msg):
    V = msg.data[0]
    AV = msg.data[1]

    # the amount of power for each velocity and turn
    if V > 0 and AV == 0:
        self.car.control_car(75, 75)
    elif V < 0 and AV == 0:
        self.car.control_car(-75, -75)
    elif V == 0 and AV > 0:
        self.car.control_car(75, -75)
    elif V == 0 and AV < 0:
        self.car.control_car(-75, 75) 
    else:
        self.car.control_car(0, 0)

def main(args=None):
  rclpy.init(args=args)
  
  subscriber = MCN()
  
  try:
    rclpy.spin(subscriber)
  except KeyboardInterrupt as e:
    print(e)
    subscriber.car.stop()
  except Exception as e:
    print(e)
    subscriber.car.stop()
  
  subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()