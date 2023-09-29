import rclpy
from rclpy.node import Node
import os
import csv
from std_msgs.msg import Float32MultiArray
import smbus
import time
import math


class Log(Node):
    def __init__(self):
        super().__init__('log')
        self.log_subscription = self.create_subscription(Float32MultiArray, '/log', self.data_callback, 10)
        self.x = 0
        self.y = 0
        self.theta = 0
        self.prevTime = 0

        self.stop = False

        self.mem = []

        #find new file for runs
        i = 0
        while os.path.exists(f"./pathlogs/logs_run{i}.csv"):
            i+=1

        #open file
        self.file = open(f"./pathlogs/logs_run{i}.csv", 'w')

        self.writer = csv.writer(self.file)

    def data_callback(self, msg):

        v = msg.data[0]
        av = msg.data[1]
        t = msg.data[2] - self.prevTime

        xV = v * math.sin(self.theta)
        yV = v * math.cos(self.theta)

        self.x += xV * t
        self.y += yV * t
        self.theta += av * t

        #writes data x pos, y pos, angle, and then the time stamp from 0
        self.writer.writerow([self.x,self.y,self.theta,msg.data[2]])

        self.prevTime = msg.data[2]


def main(args=None):
    rclpy.init(args=args)

    subscriber = Log()

    try:
        rclpy.spin(subscriber)
    except KeyboardInterrupt as e:
        print(e)
        subscriber.file.close()
    except Exception as e:
        print(e)
        subscriber.file.close()

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
