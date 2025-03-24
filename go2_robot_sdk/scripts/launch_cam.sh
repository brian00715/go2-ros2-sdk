gst-launch-1.0 udpsrc address=230.1.1.1 port=1720 multicast-iface=eth0 ! queue ! application/x-rtp, media=video, encoding-name=H264 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink &

source ./install/setup.bash
ros2 run go2_robot_sdk keyboard_ctrl