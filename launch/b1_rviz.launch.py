from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
import xacro
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # B1 description loading from xacro
    pkg_path = get_package_share_directory("b1_description")
    xacro_path = os.path.join(pkg_path, 'xacro/robot.xacro')
    assert os.path.exists(xacro_path), "The robot.xacro doesn't exist in " + str(xacro_path)
    doc = xacro.process_file(
        xacro_path,
        mappings={
            'DEBUG': 'false',
            'SENSORS': 'true',
            'LIDAR': 'true',
            'CAMERAS': 'true'
        }
    )
    robot_desc = doc.toprettyxml(indent='  ')

    robot_state_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_desc
        }]
    )

    joint_state_pub = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    rviz = Node(
            package='rviz2',
            namespace='',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', [os.path.join(pkg_path, 'rviz', 'ros2_check_joint.rviz')]]
    )
    
    return LaunchDescription([joint_state_pub, robot_state_pub, rviz])