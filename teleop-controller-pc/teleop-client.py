import sys
from roslibpy import Ros, Topic, Message
from pynput.keyboard import Key, KeyCode, Listener as KeyboardListener

from messages import VelocityMessage, STOP_MESSAGE, FORWARD_MESSAGE, BACKWARD_MESSAGE, LEFT_MESSAGE, RIGHT_MESSAGE

class RobotTeleOperator:
    def __init__(self, ros_client: Ros):
        self.ros_client = ros_client
        self.last_key_pressed = None
        self.is_key_down = False
    
    def start(self):
        self.ros_client.run()
        self.publisher = Topic(self.ros_client, '/motor_control', VelocityMessage.message_type)
    
    def __send_message(self, message: Message):
        if self.ros_client.is_connected:
            self.publisher.publish(message)
        else:
            raise Exception("Could not send message. ROS is not connected.")
    
    def stop(self):
        if self.ros_client.is_connected:
            self.stop_robot()
            self.publisher.unadvertise()
            self.ros_client.terminate()

    def on_forward(self):
        self.__send_message(FORWARD_MESSAGE)

    def on_backward(self):
        self.__send_message(BACKWARD_MESSAGE)

    def on_left(self):
        self.__send_message(LEFT_MESSAGE)

    def on_right(self):
        self.__send_message(RIGHT_MESSAGE)

    def stop_robot(self):
        self.__send_message(STOP_MESSAGE)

    def on_press(self, key):
        if (key == None or self.is_key_down):
            return

        match key:
            case KeyCode():
                pressed_key = key.char
            case _ as pressed_key:
                pass

        match pressed_key:
            case 'w':
                self.on_forward()
            case 's':
                self.on_backward()
            case 'a':
                self.on_left()
            case 'd':
                self.on_right()
            case Key.esc:
                return False
            case _:
                return
        
        self.last_key_pressed = pressed_key
        self.is_key_down = True


    def on_release(self, key):
        if key == None:
            return
        
        match key:
            case KeyCode():
                released_key = key.char
            case _ as released_key:
                pass
            
        if (released_key == self.last_key_pressed):
            self.last_key_pressed = None
            self.is_key_down = False
            self.stop_robot()


def print_controls():
    print("Teleop Client")
    print("Press 'w' to move forward")
    print("Press 'a' to move left")
    print("Press 's' to move backward")
    print("Press 'd' to move right\n")
    print("Commands will be sent to the robot as long as this process is running.")

def main(argv):
    if len(argv) < 1:
        print("Usage: python3 teleop-client.py <ROS IP Address>")
        exit(1)

    try:
        ros = Ros(argv[0], 9090)
        teleop = RobotTeleOperator(ros)
        teleop.start()

        print_controls()
        with KeyboardListener(on_press=teleop.on_press, on_release=teleop.on_release) as key_listener:
            key_listener.join()

        exit_program(teleop)
    except KeyboardInterrupt:
        exit_program(teleop)

def exit_program(teleoperator: RobotTeleOperator):
    print("\nTerminating Teleop Client...")
    teleoperator.stop()

if __name__ == '__main__':
    main(sys.argv[1:])
