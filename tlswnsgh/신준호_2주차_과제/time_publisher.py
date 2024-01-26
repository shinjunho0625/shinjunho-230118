#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('my_time', String, queue_size=10)
	rospy.init_node('talker_node', anonymous=True)
	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		now = rospy.get_rostime()
		pub.publish("{0} {1}".format(now.secs, now.nsecs))
		rospy.loginfo("==Pusblishing time : {0} {1}".format(now.secs, now.nsecs))
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass