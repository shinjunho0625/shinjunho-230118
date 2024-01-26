#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

class Time:
    def __init__(self):
        self.clock = None
        self.sub = rospy.Subscriber("my_time", String, self.callback)
        rospy.init_node('listener_node', anonymous = True)
        rospy.spin()

    def callback(self, data):
        self.clock = data.data
        rospy.loginfo(self.clock)

if __name__ == "__main__":
    try:
        call_back = Time()
        call_back.callback()
    except rospy.ROSInterruptException:
        pass
