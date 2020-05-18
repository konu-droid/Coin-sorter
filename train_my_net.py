from time import sleep as delay
import time
import cv2 
import numpy as np
import pickle

def relu(x):
    x[x<0] = 0
    return x

def driv_relu(x):
    x[x<0]=0
    x[x>0]=1
    return x

if __name__ == "__main__":

    # learning rate
    lr = 0.01

    # number of nodes
    N,H1,H2,O = 57600,100,50,5       

    # initialize weights 
    w1 = np.random.rand(N,H1)
    w2 = np.random.rand(H1,H2)
    w3 = np.random.rand(H2,O)

    # initialize bias terms
    b1 = np.random.rand(1,H1)
    b2 = np.random.rand(1,H2)
    b3 = np.random.rand(1,O)

    start = time.time()
    j = 1

    for j in range(3):
        for i in range(10):   
            file_path = '/home/konu/Documents/practice/raspberry-pi_codes/coin_sorter/coin_dataset/' + str(j) + '_coin/coin' + str(i) + '.jpg'
            frame = cv2.imread(file_path,0)

            #target
            target = np.array([1.0,0.0,0.0,0.0])

            # pre processing input
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
            output = relu(z3)
            print(output)

            #loss function
            error = (output - target)**2
            loss = error.sum()
            print(loss)

            #grad of output weights
            driv_errorO = 2*(output-target)
            driv_z3 = driv_relu(z3)
            y3 = driv_errorO*driv_z3
            loss_o = np.matmul(a2.transpose(),y3)

            #grad of H2 weights
            driv_errorH2 = np.matmul(y3,w3.transpose())
            driv_z2 = driv_relu(z2)
            y2 = driv_errorH2*driv_z2
            loss_H2 = np.matmul(a1.transpose(),y2)

            #grad of H1 weights
            driv_errorH3 = np.matmul(y2,w2.transpose())
            driv_z1 = driv_relu(z1)
            y1 = driv_errorH3*driv_z1
            loss_H1 = np.matmul(myInput.transpose(),y1) 

            #weights update
            w3 -= (lr*loss_o)
            w2 -= (lr*loss_H2)
            w1 -= (lr*loss_H1)

    #saving the network variables
    with open('trained_weight.pickle', 'wb') as f:
        pickle.dump([w1,w2,w3], f)
    with open('trained_bias.pickle', 'wb') as f:
        pickle.dump([b1,b2,b3], f)

    end = time.time()
    print(10/(end-start))
    cv2.destroyAllWindows
