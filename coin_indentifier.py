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
GPIO.setmode(GPIO.BCM) 

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

with open('/home/pi/Desktop/trained_values/old/trained_weight.pickle', 'rb') as f:
    w1,w2,w3 = pickle.load(f)
    
with open('/home/pi/Desktop/trained_values/old/trained_bias.pickle', 'rb') as f:
    b1,b2,b3 = pickle.load(f)


def relu(x):
    x[x<0] = 0
    return x

#PUT A WHILE LOOP HERE WITH ONE OF THE GPOI PINS TO SWITCH IT ON AND OFF.

# created a *threaded *video stream, allow the camera sensor to warmup,
#vs = PiVideoStream().start()
#time.sleep(2.0)

frame = cv2.imread("/home/pi/Desktop/coin_dataset_old/1_coin/coin10.jpg")
cv2.imshow('frame',frame)

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
output = z3
print(output)
print("")
print("")

if(output[0][0] > output[0][1] and output[0][0] > output[0][2] and output[0][0] > output[0][3]):
    print("Rs 1")
    GPIO.setup(17,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
    p = GPIO.PWM(17, 50)     # Sets up pin 11 as a PWM pin
    p.start(0)
    p.ChangeDutyCycle(3)  
    time.sleep(5)
elif(output[0][1] > output[0][0] and output[0][1] > output[0][2] and output[0][1] > output[0][3]):
    print("Rs 2")
    GPIO.setup(17,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
    p = GPIO.PWM(17, 50)     # Sets up pin 11 as a PWM pin
    p.start(0)
    p.ChangeDutyCycle(20) 
    time.sleep(5)
elif(output[0][2] > output[0][1] and output[0][2] > output[0][0] and output[0][2] > output[0][3]):
    print("Rs 5")
    GPIO.setup(17,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
    p = GPIO.PWM(17, 50)     # Sets up pin 11 as a PWM pin
    p.start(0)
    p.ChangeDutyCycle(40)   
    time.sleep(5)
elif(output[0][3] > output[0][1] and output[0][3] > output[0][2] and output[0][3] > output[0][0]):
    print("Rs 10")
    GPIO.setup(17,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
    p = GPIO.PWM(17, 50)     # Sets up pin 11 as a PWM pin
    p.start(0)
    p.ChangeDutyCycle(60)   
    time.sleep(5)
 
# do a bit of cleanup
cv2.destroyAllWindows()
#vs.stop()
p.stop()                 # At the end of the program, stop the PWM
GPIO.cleanup() 
