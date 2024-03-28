cmake_minimum_required(VERSION 3.5)
project(b1_description)

find_package(catkin QUIET)
find_package(ament_cmake QUIET)

find_package(sensors_description REQUIRED)

if(${catkin_FOUND})

    catkin_package()

    set(SHARE_DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

elseif(${ament_cmake_FOUND})

    ament_package()

    set(SHARE_DESTINATION share/${PROJECT_NAME})

endif()

# Install directories
set(directories launch config meshes rviz xacro)
foreach(dir IN LISTS directories)
    install(
        DIRECTORY ${dir}
        DESTINATION ${SHARE_DESTINATION}
    )
endforeach()

