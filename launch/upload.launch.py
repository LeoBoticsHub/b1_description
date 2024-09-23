from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition

from ament_index_python.packages import get_package_share_directory

import xacro
import os

def generate_launch_description():

    # Args
    use_rviz = LaunchConfiguration('use_rviz')

    DeclareLaunchArgument(
        'use_rviz',
        default_value='False'
    )

    tf_namespace = LaunchConfiguration('tf_namespace')

    tf_ns_arg = DeclareLaunchArgument(
        'tf_namespace',
        default_value=''
    )

    # B1 description loading from xacro
    pkg_path = get_package_share_directory("b1_description")
    xacro_path = os.path.join(pkg_path, 'xacro/robot.xacro')
    assert os.path.exists(xacro_path), "The robot.xacro doesnt exist in " + str(xacro_path)
    doc = xacro.process_file(xacro_path, mappings={'DEBUG': 'false', 'SENSORS': 'true',  'LIDAR': 'true', 'CAMERAS': 'true'})
    robot_desc = doc.toprettyxml(indent='  ')

    robot_state_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_desc,
            'frame_prefix': tf_namespace
        }]
    )

    rviz = Node(
        condition=IfCondition(use_rviz),
        package='rviz2',
        namespace='',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', [os.path.join(pkg_path, 'rviz', 'ros2_robot_description.rviz')]]
    )
    
    return LaunchDescription([tf_ns_arg, robot_state_pub, rviz])