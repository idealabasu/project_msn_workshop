FROM osrf/ros:humble-desktop
# WORKDIR /temp
    
ENV ROS_DOMAIN_ID=0
ENV ROS_LOCALHOST_ONLY=0
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ENV CYCLONEDDS_URI=/root/shared/cyclonedds_pc.xml

RUN apt update && \ 
    apt install -y \ 
    iputils-ping \ 
    software-properties-common \
    ros-humble-rmw-cyclonedds-cpp \ 
    ros-dev-tools