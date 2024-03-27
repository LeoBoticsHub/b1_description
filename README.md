# b1_description

This package contains the b1 description files

## launch files

To see the robot descriptio on rviz and interact with it:

```bash
roslaunch b1_description b1_rviz.launch sensors:=true
```

To upload robot description and start robot state publisher for rviz visualization purposes in real applications:

```bash
roslaunch b1_description upload.launch sensors:=true
```

## Environment

We recommand users to run this package in Ubuntu 20.04 and ROS noetic environment.

## Authors

The package is provided by:

* [Federico Rollo](https://github.com/FedericoRollo) [Mantainer]
