from roslibpy import Message

class VelocityMessage(Message):
    """
    Message for sending a linear velocity, in meters, and an angular velocity, in degrees.
    """

    message_type = 'std_msgs/Int32MultiArray'
    """
    The ROS message type string for this message class.
    """

    def __init__(self, lin_vel: int, ang_vel: int) -> None:
        payload = {
            'layout': {
                'dim': [{
                    'label': 'velocities',
                    'size': 2,
                    'stride': 0
                }],
                'data_offset': 0
            },
            'data': [lin_vel, ang_vel]
        }
        super().__init__(payload)

STOP_MESSAGE = VelocityMessage(0, 0)
FORWARD_MESSAGE = VelocityMessage(0.3, 0)
BACKWARD_MESSAGE = VelocityMessage(-0.3, 0)
LEFT_MESSAGE = VelocityMessage(0, -90)
RIGHT_MESSAGE = VelocityMessage(0, 90)
