#!/usr/bin/env python
 
import rospy
from std_msgs.msg import Float64
import math
mgstosend=0

#def callback():
#    global msgtosend
#    rospy.loginfo(msgtosend)

def talker():
    global mgstosend
    pub = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=10)
#    rospy.Subscriber('/robot/joint2_position_controller/goalpos', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(20) # 10hz
    temp=0.0
    while not rospy.is_shutdown():
	msgtosend=math.sin(temp)
#	rospy.Subscriber('/robot/joint2_position_controller/goalpos', Float64, callback)
	pub.publish(msgtosend)
	rospy.loginfo(msgtosend)  	
	temp=temp+0.05
	rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
