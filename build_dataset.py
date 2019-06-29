import cv2
import i2c_module as i2c
import os
import glob
import time
import shutil
import lcd
import cnn
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import keras
from keras.models import load_model
import numpy as np


size = 150
W = 2*size
H = 2*size



model = load_model('model.h5')
weights = model.get_weights()
my_cnn = cnn.cnn(img_width=W, img_height=H)

my_cnn.set_weights(weights)

lcd.lcd_init()



pin_parada = 40
pin_arranque = 37

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP)


i2c.stop()
i2c.openA1()
time.sleep(0.4)
i2c.openB1()
time.sleep(0.4)
i2c.closeA1()
i2c.closeA2()
i2c.closeB1()
i2c.closeB2()


#40 37 36 33

#arriba 36
#abajo 33
#rojo 40
#verde 37

def emptyBuffer(t,cams):
    start = time.time()
    N = len(cams)
    while time.time()-start< t:
        for i in range(N):
            cams[i].read()


def zero_pad(x, n):
    for i in range(1, 5):
        if x < 10 ** i:
            return (n - i) * '0' + str(x)


def choose_cameras(cams, empty_bw, bw_threshold):
    out = [0, 2, 4, 6]
    for i in range(4):
        s, img = cams[i].read()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        trash, img_bw = cv2.threshold(img_gray, bw_threshold, 255, cv2.THRESH_BINARY)
        l_min = 99999999999
        for j in range(4):
            diff = empty_bw[j] - img_bw
            if diff.sum() < l_min:
                l_min = diff.sum()
                out[i] = j
                print(str(i) + str(j) + str(l_min))
    print(out)
    out = [0,1,2,3]
    print(out)

    return out
    #return out



camera_0 = cv2.VideoCapture(0)
camera_0.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
camera_0.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
camera_2 = cv2.VideoCapture(2)
camera_2.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
camera_2.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

camera_4 = cv2.VideoCapture(4)
camera_4.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
camera_4.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

camera_6 = cv2.VideoCapture(6)
camera_6.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
camera_6.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

time.sleep(2)
s0, img_0 = camera_0.read()
s2, img_2 = camera_2.read()
s4, img_4 = camera_4.read()
s6, img_6 = camera_6.read()

empty0 = cv2.imread('empty/empty0.png')
empty2 = cv2.imread('empty/empty2.png')
empty4 = cv2.imread('empty/empty4.png')
empty6 = cv2.imread('empty/empty6.png')

th = 140

empty_gray0 = cv2.cvtColor(empty0, cv2.COLOR_BGR2GRAY)
trash, empty_BW0 = cv2.threshold(empty_gray0, th, 255, cv2.THRESH_BINARY)

empty_gray2 = cv2.cvtColor(empty2, cv2.COLOR_BGR2GRAY)
trash, empty_BW2 = cv2.threshold(empty_gray2, th, 255, cv2.THRESH_BINARY)

empty_gray4 = cv2.cvtColor(empty4, cv2.COLOR_BGR2GRAY)
trash, empty_BW4 = cv2.threshold(empty_gray4, th, 255, cv2.THRESH_BINARY)

empty_gray6 = cv2.cvtColor(empty6, cv2.COLOR_BGR2GRAY)
trash, empty_BW6 = cv2.threshold(empty_gray6, th, 255, cv2.THRESH_BINARY)
empty_BW = [empty_BW0, empty_BW2, empty_BW4, empty_BW6]
cam_ind = choose_cameras([camera_0, camera_2, camera_4, camera_6], empty_BW, th)


i = 0
j = 0
lcd.lcd_string("Nueces IZQ: " + str(i), lcd.LCD_LINE_1)
lcd.lcd_string("Nueces DER: " + str(j), lcd.LCD_LINE_2)
sleep_time = 0.4
sleep_time_2 = 0.1

#flag  = False
stop = False
i2c.closeB1()
i2c.closeA1()
flag = False
stop_motor = False
while stop == False:
    if GPIO.input(pin_parada) == GPIO.LOW:
        i2c.stop()
        i2c.openB1()
        i2c.openA1()
        flag = False
        time.sleep(1)
        if GPIO.input(pin_parada) == GPIO.LOW:
            stop = True
            print("Good bye")
        print("STOP")
    if GPIO.input(pin_arranque) == GPIO.LOW:
        i2c.closeB1()
        i2c.closeA1()
        time.sleep(1)
        flag = True
        i2c.go()
        print("GO")
    time.sleep(0.1)
    s0, img0 = camera_0.read()
    s2, img2 = camera_2.read()
    s4, img4 = camera_4.read()
    s6, img6 = camera_6.read()
    img_gray0 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    trash, img_BW0 = cv2.threshold(img_gray0, th, 255, cv2.THRESH_BINARY)
    img_gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    trash, img_BW2 = cv2.threshold(img_gray2, th, 255, cv2.THRESH_BINARY)
    img_gray4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
    trash, img_BW4 = cv2.threshold(img_gray4, th, 255, cv2.THRESH_BINARY)
    img_gray6 = cv2.cvtColor(img6, cv2.COLOR_BGR2GRAY)
    trash, img_BW6 = cv2.threshold(img_gray6, th, 255, cv2.THRESH_BINARY)

    diff0 = empty_BW[cam_ind[0]] - img_BW0
    diff2 = empty_BW[cam_ind[1]] - img_BW2
    diff4 = empty_BW[cam_ind[2]] - img_BW4
    diff6 = empty_BW[cam_ind[3]] - img_BW6

    thr2 = 1800000
    thr0 = 1800000
    # print("diff0"+str(diff0.sum()))
    # print("diff2"+str(diff2.sum()))
    # print("diff4"+str(diff4.sum()))
    # print("diff6"+str(diff6.sum()))
    if (diff2.sum() > thr0 or diff4.sum() > thr0) and flag:
      #  print('foto0 :' + str(diff0.sum()))
      #  print('foto2 :' + str(diff2.sum()))
      #  print('foto4 :' + str(diff4.sum()))
      #  print('foto6 :' + str(diff6.sum()))
      #  print(zero_pad(i, 6))
        dif = 150
        if stop_motor == True:
            i2c.stop()
        emptyBuffer(sleep_time,[camera_2,camera_4])
        start_pred = time.time()
        s2, img2 = camera_2.read()
        s4, img4 = camera_4.read()
        img = np.concatenate((img2, img4), axis=1)
        img = cv2.resize(img, (4 * dif, 2 * dif))

        pred = my_cnn.predict_classes(img.reshape([-1, 300, 600, 3]), batch_size=1)
        stop_pred = time.time()
        print(stop_pred-start_pred)
        print(pred)
        if pred == 1:
            i2c.closeA2()
        else:
            i2c.openA2()
        i2c.openA1()
        emptyBuffer(sleep_time_2, [camera_2, camera_4])

        # cv2.imwrite('data/nuez0_' + zero_pad(i, 6) + '.png', img0)
        cv2.imwrite('data/nuez2_' + zero_pad(i, 6) + '.png', img2)
        cv2.imwrite('data/nuez4_' + zero_pad(i, 6) + '.png', img4)
        # cv2.imwrite('data/nuez6_' + zero_pad(i, 6) + '.png', img6)
        start = time.time()
        i2c.closeA1()
        i = i + 1
        i2c.closeA1()
        lcd.lcd_string("Nueces IZQ: " + str(i), lcd.LCD_LINE_1)
        lcd.lcd_string("Nueces DER: " + str(j), lcd.LCD_LINE_2)
        if stop_motor == True:
            i2c.go()

    if (diff0.sum() > thr2 or diff6.sum() > thr2) and flag:
      #  print('foto0 :' + str(diff0.sum()))
      #  print('foto2 :' + str(diff2.sum()))
      #  print('foto4 :' + str(diff4.sum()))
      #  print('foto6 :' + str(diff6.sum()))
      #  print(zero_pad(i, 6))
        if stop_motor == True:
            i2c.stop()
        emptyBuffer(sleep_time, [camera_0, camera_6])
        start_pred = time.time()
        s2, img0 = camera_0.read()
        s4, img6 = camera_6.read()
        dif = 150
        img = np.concatenate((img0, img6), axis=1)
        img = cv2.resize(img, (4 * dif, 2 * dif))


        pred = my_cnn.predict_classes(img.reshape([-1, 300, 600, 3]), batch_size=1)
        stop_pred = time.time()
        print(stop_pred - start_pred)
        print(pred)
        if pred == 1:
            i2c.closeB2()
        else:
            i2c.openB2()
        i2c.openB1()
        emptyBuffer(sleep_time_2, [camera_0, camera_6])

        cv2.imwrite('data/nuez0_' + zero_pad(i, 6) + '.png', img0)
        # cv2.imwrite('data/nuez2_' + zero_pad(i, 6) + '.png', img2)
        # cv2.imwrite('data/nuez4_' + zero_pad(i, 6) + '.png', img4)
        cv2.imwrite('data/nuez6_' + zero_pad(i, 6) + '.png', img6)
        start = time.time()
        i2c.closeB1()

        j = j + 1
        lcd.lcd_string("Nueces IZQ: " + str(i), lcd.LCD_LINE_1)
        lcd.lcd_string("Nueces DER: " + str(j), lcd.LCD_LINE_2)
        if stop_motor == True:
            i2c.go()

exit()
