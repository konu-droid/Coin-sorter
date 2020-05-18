#513 is the tested number of steps for 1 resolution

import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
int_1 = 13# pink
int_2 = 19 # orange
int_3 = 5 # blue
int_4 = 6 # yellow
 
# adjust if different
StepCount = 8

Seq=[[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1]]
'''
Seq=[[0,1,1,1],
	[0,0,1,1],
	[1,0,1,1],
	[1,0,0,1],
	[1,1,0,1],
	[1,1,0,0],
	[1,1,1,0],
	[0,1,1,0]]
	'''
 
GPIO.setup(int_1, GPIO.OUT)
GPIO.setup(int_2, GPIO.OUT)
GPIO.setup(int_3, GPIO.OUT)
GPIO.setup(int_4, GPIO.OUT)

def setStep(w1):
    GPIO.output(int_1, w1[0])
    GPIO.output(int_2, w1[1])
    GPIO.output(int_3, w1[2])
    GPIO.output(int_4, w1[3])
    
def Stop():
	GPIO.output(int_1, 0)
	GPIO.output(int_2, 0)
	GPIO.output(int_3, 0)
	GPIO.output(int_4, 0)
 
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j])
            time.sleep(delay)
 
def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j])
            time.sleep(delay)
 
if __name__ == '__main__':
    while True:
        delay = input("Time Delay (ms)?")
        steps = input("How many steps forward? ")
        forward(int(delay) / 1000.0, int(steps))
        Stop()
        steps = input("How many steps backwards? ")
        backwards(int(delay) / 1000.0, int(steps))
        Stop()
