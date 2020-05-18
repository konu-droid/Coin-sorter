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

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=300, 
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args())             

# 57600,100,50,5 gives 14 fps and 57600,200,50,5 gives 9 fps
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

'''
with open('/home/pi/Desktop/trained_values/trained_weight.pickle', 'rb') as f:
    w1,w2,w3 = pickle.load(f)
    
with open('/home/pi/Desktop/trained_values/trained_bias.pickle', 'rb') as f:
    b1,b2,b3 = pickle.load(f)
 '''
 
def relu(x):
    x[x<0] = 0
    return x

# created a *threaded *video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from `picamera` module...")
vs = PiVideoStream().start()
time.sleep(2.0)
fps = FPS().start()
 
# loop over some frames...this time using the threaded stream
while fps._numFrames < args["num_frames"]:
	# grab the frame from the threaded video stream
	frame = vs.read()
	#print(frame.shape)
	
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
	#print(output)
    
	# check to see if the frame should be displayed to our screen
	if args["display"] > 0:
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
 
	# update the FPS counter
	fps.update()
 
# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()


