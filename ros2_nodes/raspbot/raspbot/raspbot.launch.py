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
 
    ld.add_action(MCN)
    ld.add_action(DRAC)
    
    return ld