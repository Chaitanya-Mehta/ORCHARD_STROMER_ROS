"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
import math
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
ti=time.ctime()
kit.servo[0].angle = 90
time.sleep(1)
while 1==1:
	t=time.ctime()
	crt_time=t-ti
	kit.servo[0].angle = 90 + (90*sin(t))
	pass
