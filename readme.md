# Assignment 1

## Setup

### Dependencies

#### Robot Dependencies

This robot project depends on the `rosbridge_server` package, which is available on the ROS2 apt repository. To install on the robot: `sudo apt install ros-<rosdistro>-rosbridge-server`.

#### TeleOp Client Dependencies

The TeleOp Client was written against python 3.11, though any version of python 3 that supports the `match` statement should work.

The teleop client dependencies are specified in `teleop-controller-pc/requirements.txt`. To install, run `pip3 install -r teleop-controller-pc/requirements.txt` (installation in a venv is recommended) on the computer that will be remotely controlling the robot.

### Building the ROS Package

Building the ROS package is only required when cloning the repository or when new nodes/files are added. To build:

* Ensure you have sourced the ROS setup script (`/opt/ros/<distro>/setup.bash`) for the ROS distro you are using.
* From the root of the repository, run the `buildpackage.sh` script. OR, if that doesn't work, Navigate to the `ros2_nodes/raspbot` directory and run `colcon build --symlink-install` to build the package.

## Running the Robot Programs

### Running Robot Nodes

Make sure you've sourced the ROS setup script (`/opt/ros/<distro>/setup.bash`) before running any robot nodes or scripts on the robot.

In the root of the repo are two shell scripts to ease running the robot nodes. You can run these scripts from the root of the repo, or you can run the commands manually as described below after you have followed the steps to build the ROS package.

1. Build the ROS package if you haven't already.
2. Source the `install/local_setup.bash` if you haven't already for the existing shell session.
3. Run the program using `ros2 launch raspbot <program_launch_file>` where `<program_launch_file>` is the name of the launch file for the program you want to run as described below:
    - `square_launch.xml`: Launches the square program, which moves the robot in a square. Robot moves 2 seconds before each turn.
    - `teleop_launch.xml`: Launches the teleop program, which allows for robot control from a remote machine connecting through the teleop client (see below).

### Running TeleOp Client

The TeleOp Client is a regular python script. It can run from any machine with the needed dependencies installed (as described above). You will need to be on the same network as the robot to connect to it and will need to have the robot's IP address or hostname.

* Ensure you have a recent version of python that supports the `match` statement installed.
* To run the teleop node, on the machine that will control the robot, install the python packages in `teleop-controller-pc/requirements.txt` using pip.
* After installing the required packages, from the `teleop-controller-pc` directory, run `python3 teleop.py <robot-network-address>` to start the teleop node.
* After the teleop client is running, you can control the robot with the displayed controls. To stop the robot
and exit teleop control, press ESC or CTRL+C.

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

## Calibrations used for robot motors

At 75 power the robot moves at .3 meters per second
At 75 power turning the robot moves ~90 degrees per second
