# import the necessary packages
from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import imutils
import time
import cv2
import numpy as np
import pickle
import RPi.GPIO as GPIO  
from time import sleep  
import serial
 
GPIO.setmode(GPIO.BCM)
ser=serial.Serial("/dev/ttyACM0",9600)
ser.baudrate=9600

#amount of coins
count = 0

# learning rate
lr = 0.01             

# Number of nodes
N,H1,H2,O = 57600,100,50,5

# initialize tensor variables for weights 
w1 = np.random.rand(N,H1)
w2 = np.random.rand(H1,H2)
w3 = np.random.rand(H2,O)

# initialize tensor variables for bias terms
b1 = np.random.rand(1,H1)
b2 = np.random.rand(1,H2)
b3 = np.random.rand(1,O)

with open('/home/pi/Desktop/trained_values/trained_weight.pickle', 'rb') as f:
    w1,w2,w3 = pickle.load(f)
    
with open('/home/pi/Desktop/trained_values/trained_bias.pickle', 'rb') as f:
    b1,b2,b3 = pickle.load(f)

def relu(x):
    x[x<0] = 0
    return x

#PUT A WHILE LOOP HERE WITH ONE OF THE GPOI PINS TO SWITCH IT ON AND OFF.

# created a *threaded *video stream, allow the camera sensor to warmup,
vs = PiVideoStream().start()
time.sleep(2.0)

# Set up pin 11 for PWM
GPIO.setup(19,GPIO.OUT) 
p = GPIO.PWM(19, 50)     
p.start(0)

while True:
	
	# grab the frame from the threaded video stream
	frame = vs.read()
	#frame = cv2.imread("/home/pi/Desktop/coin_dataset/2_coin/coin10.jpg")
		
	#neural net code
	# initialize tensor for inputs
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frame = frame.reshape(1,-1)
	myInput = frame.astype(np.float64)
	myInput = myInput/255
	#print(myInput)

	# activation of H1 layer 
	z1 = np.matmul(myInput, w1)/N + b1
	a1 = relu(z1)

	# activation of H2 layer
	z2 = np.matmul(a1,w2)/H1 + b2
	a2 = relu(z2)
		
	#activation of O layer
	z3 = np.matmul(a2,w3)/H2 + b3
	#output = z3
	print(z3)
	
	output = np.where(z3 == np.amax(z3))
	print(output[0])
	
	if(output[0] == 0):
		ser.write('a')
		sleep(1)
	else if(output[0] == 1):
		ser.write('b')
		sleep(1)
	else if(output[0] == 2):
		ser.write('c')
		sleep(1)
	else if(output[0] == 3):
		ser.write('d')
		sleep(1)
	else:
		ser.write('n')
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
p.stop()
GPIO.cleanup() 

