# import the necessary packages
from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import imutils
import time
import cv2
import numpy as np
import RPi.GPIO as GPIO

# created a *threaded *video stream, allow the camera sensor to warmup,
print("[INFO] sampling THREADED frames from `picamera` module...")
vs = PiVideoStream().start()
time.sleep(2.0)

#amount of coin being recorded
j = 10

#put here the last number of the photo
new_val = 0 

#Number of photos per iteration
n = 1

while True:
	for i in range(n):
		time.sleep(0.3)
		frame = vs.read()
		print(i+new_val)
		b = '/home/pi/Desktop/coin_dataset/' + str(j) + '_coin/coin' + str(i+new_val) +'.jpg'
		cv2.imwrite(b,frame)
		if True:
			cv2.imshow("Frame", frame)
			key = cv2.waitKey(1) & 0xFF
					
	question = input("More y/n?")
	if question == 'n':
		break
	else:
		new_val+=n
	
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()

