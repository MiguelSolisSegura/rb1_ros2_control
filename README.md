# RB1 Robot ROS2 Control Integration

## Introduction

The RB1 ROS2 Control package is designed to facilitate the simulation and control of the RB1 robot using ROS2 Control framework and Gazebo. This package includes integration of ROS2 control for differential drive, and the elevator usage instructions the Gazebo environment. Users can expect a seamless transition between simulation and real-world application with standardized control interfaces.

## Installation Instructions

### Prerequisites
- ROS2 Foxy or later
- Gazebo simulation environment
- Git

### Setup and Installation
1. Clone the repository and navigate to your workspace:
   ```bash
   cd ~/ros2_ws/src
   git clone https://github.com/MiguelSolisSegura/rb1_ros2_description.git
   ```
2. Compile the code to ensure all dependencies are properly integrated:
   ```bash
   cd ~/ros2_ws
   colcon build
   source install/setup.bash
   ```

## Getting Started

To launch the simulation:
1. Start Gazebo with the RB1 robot simulation:
   ```bash
   ros2 launch rb1_ros2_description rb1_ros2_xacro.launch.py
   ```
   Note: If Gazebo fails to start, or there are any errors related to the control nodes, terminate the process using `Ctrl + C` and retry launching the file.

## Controller Activation

To activate the controllers for the robot:
1. Ensure that the ROS2 control nodes and the controllers are running correctly:
   ```bash
   ros2 control list_hardware_interfaces
   ros2 control list_controllers
   ```
2. You should see a list of command/state interfaces and two active controllers respectively.

## Operating the Robot

### Moving the Differential Drive
- To control the robot motion using the differential drive plugin:
  ```bash
  ros2 topic pub --rate 30 /diffbot_base_controller/cmd_vel_unstamped geometry_msgs/msg/Twist "{linear: {x: 0.5, y: 0, z: 0.0}, angular: {x: 0.0,y: 0.0, z: 0.5}}"
  ```
  Adjust the command as necessary to include specific values for linear and angular velocities.

### Manipulating the Lifting Unit
- The lifting effort value has SI force units (N).
- Adjust this value accordingly to your load.
- To move the lifting unit up, when unloaded:
  ```bash
  ros2 service call /apply_joint_effort gazebo_msgs/srv/ApplyJointEffort '{joint_name: "robot_elevator_platform_joint", effort: 1.0, start_time: {sec: 0, nanosec: 0}, duration: {sec: -1, nanosec: 0} }'
  ```
- To move the lifting unit down:
  ```bash
  ros2 service call /apply_joint_effort gazebo_msgs/srv/ApplyJointEffort '{joint_name: "robot_elevator_platform_joint", effort: -1.0, start_time: {sec: 0, nanosec: 0}, duration: {sec: -1, nanosec: 0} }'
  ```
