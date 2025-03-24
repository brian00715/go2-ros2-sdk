#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import sys, select, termios, tty
import time

settings = termios.tcgetattr(sys.stdin)

msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >

t : up (+z)
b : down (-z)

Robot Control:
1 : stand up
2 : crush down

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit
"""

moveBindings = {
    "i": (1, 0, 0, 0),
    "o": (1, 0, 0, -1),
    "j": (0, 0, 0, 1),
    "l": (0, 0, 0, -1),
    "u": (1, 0, 0, 1),
    ",": (-1, 0, 0, 0),
    ".": (-1, 0, 0, 1),
    "m": (-1, 0, 0, -1),
    "O": (1, -1, 0, 0),
    "I": (1, 0, 0, 0),
    "J": (0, 1, 0, 0),
    "L": (0, -1, 0, 0),
    "U": (1, 1, 0, 0),
    "<": (-1, 0, 0, 0),
    ">": (-1, -1, 0, 0),
    "M": (-1, 1, 0, 0),
    "t": (0, 0, 1, 0),
    "b": (0, 0, -1, 0),
}

speedBindings = {
    "q": (1.1, 1.1),
    "z": (0.9, 0.9),
    "w": (1.1, 1),
    "x": (0.9, 1),
    "e": (1, 1.1),
    "c": (1, 0.9),
}


def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def vels(speed, turn):
    return "currently:\tspeed %s\tturn %s " % (speed, turn)


def main(args=None):
    if args is None:
        args = sys.argv

    rclpy.init(args=args)
    node = rclpy.create_node("teleop_twist_keyboard")

    pub = node.create_publisher(Twist, "cmd_vel", 10)
    joy_pub = node.create_publisher(Joy, "joy", 10)

    speed = 0.5
    turn = 1.0
    x = 0
    y = 0
    z = 0
    th = 0
    status = 0

    try:
        print(msg)
        print(vels(speed, turn))
        while True:
            if not rclpy.ok():
                break
                
            key = getKey()
            if key == "1":  # Stand up command
                joy_msg = Joy()
                joy_msg.header.stamp = node.get_clock().now().to_msg()
                joy_msg.buttons = [0] * 15  # Initialize buttons array
                joy_msg.axes = [0.0] * 8  # Initialize axes array
                joy_msg.buttons[0] = 1  # Button A for stand up
                joy_pub.publish(joy_msg)
                time.sleep(0.1)  # Add small delay for message processing
            elif key == "2":  # Crush down command
                joy_msg = Joy()
                joy_msg.header.stamp = node.get_clock().now().to_msg()
                joy_msg.buttons = [0] * 15  # Initialize buttons array
                joy_msg.axes = [0.0] * 8  # Initialize axes array
                joy_msg.buttons[1] = 1  # Button B for crush down
                joy_pub.publish(joy_msg)
                time.sleep(0.1)  # Add small delay for message processing
            elif key in moveBindings.keys():
                x = moveBindings[key][0]
                y = moveBindings[key][1]
                z = moveBindings[key][2]
                th = moveBindings[key][3]
            elif key in speedBindings.keys():
                speed = speed * speedBindings[key][0]
                turn = turn * speedBindings[key][1]

                print(vels(speed, turn))
                if status == 14:
                    print(msg)
                status = (status + 1) % 15
            else:
                x = 0
                y = 0
                z = 0
                th = 0
                if key == "\x03":
                    break

            twist = Twist()
            twist.linear.x = x * speed
            twist.linear.y = y * speed
            twist.linear.z = z * speed
            twist.angular.x = 0.0
            twist.angular.y = 0.0
            twist.angular.z = th * turn
            pub.publish(twist)

    except Exception as e:
        print(e)

    finally:
        twist = Twist()
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        pub.publish(twist)

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
