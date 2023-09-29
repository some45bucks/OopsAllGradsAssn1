from launch import LaunchDescription
from launch_ros.actions import Node
 
def generate_launch_description():
    ld = LaunchDescription()
    #just add your files like this and they should all run
    
    MCN = Node(
        package="raspbot",
        executable="MCN",
        name='MCN'
    )

    DRAC = Node(
        package="raspbot",
        executable="DRAC",
        name='DRAC'
    )

    IMU = Node(
        package="raspbot",
        executable="IMU",
        name='IMU'
    )

    # Log = Node(
    #     package="raspbot",
    #     executable="log",
    #     name='log'
    # )
 
    ld.add_action(MCN)
    ld.add_action(DRAC)
    ld.add_action(IMU)
    #ld.add_action(Log)
    
    return ld