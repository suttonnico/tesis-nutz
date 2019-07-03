import cv2
import i2c_module as i2c
import os
import glob
import time
import shutil
import lcd
#import cnn
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from recinto import Recinto

size = 150
W = 2*size
H = 2*size



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


recinto1 = Recinto(2,4,i2c.openA1,i2c.closeA1,i2c.stop,i2c.go,lcd.LCD_LINE_1,3000000)
recinto2 = Recinto(0,6,i2c.openB1,i2c.closeB1,i2c.stop,i2c.go,lcd.LCD_LINE_2,1500000)
#flag  = False
stop = False
i2c.closeB1()
i2c.closeA1()
flag = False
stop_motor = True
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
    recinto1.take_photos()
    recinto2.take_photos()

exit()
