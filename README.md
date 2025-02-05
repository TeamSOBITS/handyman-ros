# ROS2 Package for Handyman

This project is ROS2 package for the Handyman task of the RoboCup@Home Simulation.

See also [wiki page](https://github.com/RoboCupatHomeSim/handyman-ros/wiki).


## Prerequisites

Same as below for OS and ROS2 version.  
https://github.com/RoboCupatHomeSim/documents/blob/master/SoftwareManual/Environment.md#ubuntu-pc

## How to Install

### Install Rosbridge Server

Please see below.  
http://wiki.ros.org/rosbridge_suite

### Install SIGVerse Rosbridge Server

Please see below.  
https://github.com/SIGVerse/ros_package/tree/humble-devel/sigverse_ros_bridge

### Install ROS Package of Handyman

```bash:
$ cd ~/colcon_ws/src
$ git clone -b humble-devel https://github.com/RoboCupatHomeSim/handyman-ros.git
$ cd ..
$ colcon build
```

## How to Execute

### How to Execute Sample ROS2 Node

It is a simple ROS2 node that communicates with the Handyman application.

```bash:
$ ros2 launch handyman_ros sample.launch.py
```

### How to Execute Teleoperation Tool

You can operate HSR with keyboard operation.  
It is for debugging.

```bash:
$ ros2 launch handyman_ros teleop_key.launch.py
```

## License

This project is licensed under the SIGVerse License - see the LICENSE.txt file for details.
