# Assignment 1

## Setup

### Building ROS Package

Building the ROS package is only required when cloning the repository or when new nodes are added. To build:

* Navigate to the `ros2_nodes/raspbot` directory and run `colcon build --symlink-install` to build the package.

### Using the Nodes

* To use the nodes, first source the `install/local_setup.bash` if you haven't already for the existing shell session.
* Run nodes using `ros2 run raspbot <node name here>`

## Info about sonar

* Power Supply :+5V DC
* Quiescent Current : <2mA
* Working Current: 15mA
* Effectual Angle: <15°
* Ranging Distance : 2cm – 400 cm/1″ – 13ft
* Resolution : 0.3 cm
* Measuring Angle: 30 degree
* Trigger Input Pulse width: 10uS TTL pulse
* Echo Output Signal: TTL pulse proportional to the distance range
* Dimension: 45mm x 20mm x 15mm

At 75 power the robot moves at .3 meters per second
At 75 power turning the robot moves ~90 degrees per second
