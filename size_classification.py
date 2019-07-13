import numpy as np
import cv2
from skimage.feature import canny
import math
import time

def sizes2rad(size1,size2,T):
    tv = 0.51
    L = 20
    print(T)
    t1 = math.atan(size1 / T * math.tan(tv))
    print("tita 1:"+str(t1))
    t2 = math.atan(size2 / T * math.tan(tv))
    print("tita 2:" + str(t2))
    h1 = L / (math.cos(t1)+math.sin(t1)/math.tan(t2))
    return math.sin(t1)*h1


def addUp(x,dif):
    a = np.average(x[0:dif,0:dif,0])
    b = np.average(x[0:dif,0:dif,1])
    c = np.average(x[0:dif, 0:dif,2])
    return [a,b,c]


def diffInColor(x,y):
    x= [int(x[0]),int(x[1]),int(x[2])]
    y = [int(y[0]), int(y[1]), int(y[2])]
   # print('X:'+str(x))
   # print('Y:' + str(y))

    R = np.abs(x[0] - y[0])
    G = np.abs(x[1] - y[1])
    B = np.abs(x[2] - y[2])
  #  print([R,G,B])
    dif = (R + G + B)/3
    th = 40

    if (np.abs(R-G)<th) & (np.abs(R-B) <th) & (np.abs(G-B) <th):
        dif = dif*0.001
    if dif > 255:
        dif = 255
    dif = dif/255
    return dif

def diffInColor2(R,G,B):
    R = int(R)
    G = int(G)
    B = int(B)
    dif = (R + G + B)/3
    th = 40

    if (np.abs(R - G) < th) & (np.abs(R - B) < th) & (np.abs(G - B) < th):
        dif = dif * 0.001
    if dif > 255:
        dif = 255
    dif = dif / 255
    return dif

def findRadius(img,empty):
    start=time.time()
    kernel = np.ones((5, 5), np.uint8)
    [N, M, D] = np.shape(img)
    diff = np.zeros([N, M])
    step = 10
    div = 2
    img_small = cv2.resize(img, (int(120/div), int(160/div)))
    empty_small = cv2.resize(empty,(int(120/div), int(160/div)))
    diff_pre = np.abs(img_small-empty_small)
    vdiff = np.vectorize(diffInColor2)
    diff =vdiff(diff_pre[:,:,0],diff_pre[:,:,1],diff_pre[:,:,2])
    #print(diff)
    #for i in range(int(N / step)):
    #    for j in range(int(M / step)):
    #        diff[i * step:i * step + step, j * step:j * step + step] = diffInColor(
    #            addUp(img[i * step:i * step + step, j * step:j * step + step], step),
    #            addUp(empty[i * step:i * step + step, j * step:j * step + step], step))
    its = 3
    diff = cv2.dilate(diff, kernel, iterations=its)
    diff = cv2.erode(diff, None, iterations=its)
    th = 0.2

    trash, diff = cv2.threshold(diff, th, 1, cv2.THRESH_BINARY)
    edges = canny(diff, sigma=6)
    [y_edges,x_edges] = np.nonzero(edges)
    y_min = np.min(y_edges)
    y_max = np.max(y_edges)
    x_min = np.min(x_edges)
    x_max = np.max(x_edges)
    #cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 3)
    print("tiempo en la clasifiacion por imagenes: "+str(time.time()-start))

    return y_max-y_min