import cv2
import serie as i2c
import os
import glob
import time
import shutil
import lcd
import cnn
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from recinto import Recinto
from keras.models import load_model
import threading
import fileLibrary
import predictor

display = fileLibrary.nueces_data()
display.set_clasif_buenas_value(0)
display.set_clasif_malas_value(0)
display.set_config_value(3)
display.set_subclasif_buenas_chicas_value(0)
display.set_subclasif_buenas_grandes_value(0)

size = 150
W = 160
H = 120




weights = load_model('model_sep_0.h5').get_weights()
my_cnn_0 = cnn.cnn_sep(img_width=W, img_height=H)
my_cnn_0.set_weights(weights)
weights = load_model('model_sep_6.h5').get_weights()
my_cnn_6 = cnn.cnn_sep(img_width=W, img_height=H)
my_cnn_6.set_weights(weights)
weights = load_model('model_sep_2.h5').get_weights()
my_cnn_2 = cnn.cnn_sep(img_width=W, img_height=H)
my_cnn_2.set_weights(weights)
weights = load_model('model_sep_4.h5').get_weights()
my_cnn_4 = cnn.cnn_sep(img_width=W, img_height=H)
my_cnn_4.set_weights(weights)

predictor_0_6 = predictor.predictor(my_cnn_0, my_cnn_6)
predictor_2_4 = predictor.predictor(my_cnn_2, my_cnn_4)
#lcd.lcd_init()



pin_parada = 40
pin_arranque = 37
pin_arriba = 36
pin_abajo = 33

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP)


i2c.stop()


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


recinto1 = Recinto(2, 4, open=i2c.openA1, close=i2c.closeA1, stop=i2c.stop, go=i2c.go, thNut=1300000, model=predictor_2_4,
                   size=size, bad=i2c.ABad, small=i2c.ASmall, big=i2c.ABig)
recinto2 = Recinto(0, 6, open=i2c.openB1, close=i2c.closeB1, stop=i2c.stop, go=i2c.go, thNut=1200000, model=predictor_0_6,
                   size=size, bad=i2c.BBad, small=i2c.BSmall, big=i2c.BBig)

#flag  = False
display.set_clasif_buenas_value(0)
display.set_clasif_malas_value(0)
display.set_config_value(3)
display.set_subclasif_buenas_chicas_value(0)
display.set_subclasif_buenas_grandes_value(0)

stop = False
i2c.closeB1()
i2c.closeA1()
flag = False
stop_motor = True
motor = False
thread1 = threading.Thread(target = recinto1.take_photos())
thread2 = threading.Thread(target = recinto2.take_photos())
print("LISTO")
while stop == False:
    if GPIO.input(pin_arriba) == GPIO.LOW:
        recinto1.up_calibre()
        recinto2.up_calibre()
        cal=float(display.get_config_value())
        display.set_config_value(cal+0.1)
        print("CALIBRE:"+str(recinto1.calibre))
    if GPIO.input(pin_abajo)== GPIO.LOW:
        recinto1.dw_calibre()
        recinto2.up_calibre()
        cal = float(display.get_config_value())
        if cal > 0:
            display.set_config_value(cal - 0.1)
        print("CALIBRE:"+str(recinto1.calibre))
    if GPIO.input(pin_parada) == GPIO.LOW:
        i2c.stop()
        i2c.openB1()
        i2c.openA1()
        flag = False
        time.sleep(1)
        motor = False
        if GPIO.input(pin_parada) == GPIO.LOW:
            stop = True
            print("Good bye")
        print("STOP")
    if GPIO.input(pin_arranque) == GPIO.LOW:
        i2c.closeB1()
        i2c.closeA1()
        time.sleep(1)
        flag = True
        motor = True
        i2c.go()
        print("GO")
    time.sleep(0.1)
    if motor:
        if thread1.is_alive() == False:
            thread1 = threading.Thread(target=recinto1.take_photos)
            thread1.start()
        if thread2.is_alive() == False:
            thread2 = threading.Thread(target=recinto2.take_photos)
            thread2.start()



exit()
