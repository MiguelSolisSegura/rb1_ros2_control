from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, RegisterEventHandler
from launch.conditions import IfCondition
from launch.event_handlers import OnProcessExit
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():


    robot_controllers = PathJoinSubstitution(
        [
            FindPackageShare("rb1_ros2_description"),
            "config",
            "rb1_controller.yaml",
        ]
    )

    control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[robot_controllers],
        output="both",
    )

    nodes = [
        control_node,
        #robot_state_pub_node,
        #joint_state_broadcaster_spawner,
        #delay_rviz_after_joint_state_broadcaster_spawner,
        #delay_robot_controller_spawner_after_joint_state_broadcaster_spawner,
    ]

    return LaunchDescription(nodes)