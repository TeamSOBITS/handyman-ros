import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    sub_msg_to_robot_topic_name = LaunchConfiguration('sub_msg_to_robot_topic_name', default='/handyman/message/to_robot')
    pub_msg_to_moderator_topic_name = LaunchConfiguration('pub_msg_to_moderator_topic_name', default='/handyman/message/to_moderator')
    sub_joint_state_topic_name = LaunchConfiguration('sub_joint_state_topic_name', default='/hsrb/joint_states')
    pub_base_twist_topic_name = LaunchConfiguration('pub_base_twist_topic_name', default='/hsrb/command_velocity')
    pub_arm_trajectory_topic_name = LaunchConfiguration('pub_arm_trajectory_topic_name', default='/hsrb/arm_trajectory_controller/command')
    pub_gripper_trajectory_topic_name = LaunchConfiguration('pub_gripper_trajectory_topic_name', default='/hsrb/gripper_controller/command')
    ros_bridge_port = LaunchConfiguration('ros_bridge_port', default='9090')

    teleop_key_handyman_node = Node(
        package='handyman_ros',
        executable='teleop_key_handyman',
        name='teleop_key_handyman',
        output='screen',
        prefix='xterm -font r16 -fg floralwhite -bg darkslateblue -e',
        parameters=[
            {'sub_msg_to_robot_topic_name': sub_msg_to_robot_topic_name},
            {'pub_msg_to_moderator_topic_name': pub_msg_to_moderator_topic_name},
            {'sub_joint_state_topic_name': sub_joint_state_topic_name},
            {'pub_base_twist_topic_name': pub_base_twist_topic_name},
            {'pub_arm_trajectory_topic_name': pub_arm_trajectory_topic_name},
            {'pub_gripper_trajectory_topic_name': pub_gripper_trajectory_topic_name}
        ]
    )

    sigverse_ros_bridge_launch_file = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('sigverse_ros_bridge'),
                'launch',
                'sigverse_ros_bridge.launch.py'
            )
        ),
        launch_arguments={'port': ros_bridge_port}.items()
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz',
        arguments=['-d', os.path.join(get_package_share_directory('handyman_ros'), 'launch', 'hsr.rviz')]
    )

    return LaunchDescription([
        DeclareLaunchArgument('sub_msg_to_robot_topic_name', default_value='/handyman/message/to_robot'),
        DeclareLaunchArgument('pub_msg_to_moderator_topic_name', default_value='/handyman/message/to_moderator'),
        DeclareLaunchArgument('sub_joint_state_topic_name', default_value='/hsrb/joint_states'),
        DeclareLaunchArgument('pub_base_twist_topic_name', default_value='/hsrb/command_velocity'),
        DeclareLaunchArgument('pub_arm_trajectory_topic_name', default_value='/hsrb/arm_trajectory_controller/command'),
        DeclareLaunchArgument('pub_gripper_trajectory_topic_name', default_value='/hsrb/gripper_controller/command'),
        DeclareLaunchArgument('sub_laser_scan_topic_name', default_value='/hsrb/base_scan'),
        DeclareLaunchArgument('rgbd_camera', default_value='head_rgbd_sensor'),
        DeclareLaunchArgument('sigverse_ros_bridge_port', default_value='50001'),
        DeclareLaunchArgument('sync_time_num', default_value='1'),
        DeclareLaunchArgument('ros_bridge_port', default_value='9090'),
        teleop_key_handyman_node,
        sigverse_ros_bridge_launch_file,
        rviz_node
    ])

