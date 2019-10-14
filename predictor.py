import cv2
import cnn
from keras.models import load_model
import os
import numpy as np


import logging

logging.basicConfig(filename='predictions.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')


def zero_pad(x,n):
    for i in range(1,5):
        if x < 10 ** i:
            return (n-i)*'0'+str(x)

def getNutId(x):
    return(x[11])

def subNutId(x,id):
    s = list(x)
    s[11] = id
    return "".join(s)

def getNutNumber(x):
    return(x[4:len(x)-6])


pairs = {
    '0':'6',
    '2':'4'
}

def getSide(x):
    return x[4]

W = 160
H = 120

class predictor:
    model_1 = {}
    model_2 = {}

    def __init__(self,model_1,model_2):
        self.model_1 = model_1
        self.model_2 = model_2

    def predict(self,img1,img2):
        p_1 = self.model_1.predict_proba(img1, 1, 0)
        p_2 = self.model_2.predict_proba(img2, 1, 0)
        print("p1: "+str(p_1)+" p2: "+str(p_2))
        logging.debug("p1: "+str(p_1)+" p2: "+str(p_2))
        if (p_1 + p_2)> 1:
            return 1
        else:
            return 0
