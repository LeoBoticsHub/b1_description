# b1_description

This package contains the b1 description files. It works both with ROS and ROS 2 distros.

## Dependencies

this package depends on the following:

* [sensors_description](https://github.com/LeoBoticsHub/sensors_description.git)

please clone it in the same workspace of b1_description.

## Launch files

To see the robot description on rviz and interact with it:

* ROS:

```bash
roslaunch b1_description b1_rviz.launch sensors:=true
```

* ROS 2:

```bash
ros2 launch b1_description b1_rviz.launch.py
```

* ROS 2 with the champ library and Gazebo simulation:

```bash
ros2 launch champ_simulation robot_sim.launch.py SENSORS:=true
ros2 launch b1_description b1_rviz_champ.launch.py
```

 * ROS 2 with the champ library and Ignition Fortrees simulation:

```bash
ros2 launch champ_simulation robot_ign_sim.launch.py SENSORS:=true
ros2 launch b1_description b1_rviz_champ.launch.py
```  

To upload robot description and start robot state publisher for rviz visualization purposes in real applications:

* ROS:

```bash
roslaunch b1_description upload.launch sensors:=true
```

* ROS 2:

```bash
ros2 launch b1_description upload.launch.py
```

## Environment

We recommand users to run this package in Ubuntu 20.04 or 22.04 and ROS noetic, Foxy or Humble envir\onment.

## Authors

The package is provided by:

* [Federico Rollo](https://github.com/FedericoRollo) [Mantainer]
* [Giuseppe Alfonso](https://github.com/GiuseppeAlfonso) [Mantainer]
