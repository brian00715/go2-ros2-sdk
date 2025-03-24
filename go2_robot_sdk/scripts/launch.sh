cp /home/unitree/go2_ros2_simon_ws/src/go2_robot_sdk/launch/* /home/unitree/go2_ros2_simon_ws/install/go2_robot_sdk/share/go2_robot_sdk/launch/
cp /home/unitree/go2_ros2_simon_ws/src/go2_robot_sdk/config/* /home/unitree/go2_ros2_simon_ws/install/go2_robot_sdk/share/go2_robot_sdk/config/

source ./install/setup.bash

# export ROBOT_IP="192.168.43.32" #for muliple robots, just split by ,
# export ROBOT_IP="192.168.12.1" #for muliple robots, just split by ,
# export CONN_TYPE="webrtc"
export ROBOT_IP="192.168.123.161" #for muliple robots, just split by ,
export CONN_TYPE="cyclonedds"

ros2 launch go2_robot_sdk robot.launch.py
