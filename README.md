# ROS Package for Handyman

This project is ROS package for the Handyman task of the RoboCup@Home Simulation.

See also [wiki page](https://github.com/RoboCupatHomeSim/handyman-ros/wiki).


## Prerequisites

Same as below for OS and ROS version.  
https://github.com/RoboCupatHomeSim/documents/blob/master/SoftwareManual/Environment.md#ubuntu-pc

## How to Install

### Install Rosbridge Server

Please see below.  
http://wiki.ros.org/rosbridge_suite

### Install SIGVerse Rosbridge Server

Please see below.  
https://github.com/SIGVerse/ros_package/tree/master/sigverse_ros_bridge

### Install ROS Package of Handyman

```bash:
$ cd ~/catkin_ws/src
$ git clone https://github.com/RoboCupatHomeSim/handyman-ros.git
$ cd ..
$ catkin_make
```

## How to Execute

### How to Execute Sample ROS Node

It is a simple ROS node that communicates with the Handyman application.

```bash:
$ roslaunch handyman sample.launch
```

### How to Execute Teleoperation Tool

You can operate HSR with keyboard operation.  
It is for debugging.

```bash:
$ roslaunch handyman teleop_key.launch
```

## License

This project is licensed under the SIGVerse License - see the LICENSE.txt file for details.
