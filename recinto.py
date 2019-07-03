import cv2
import i2c_module as i2c
import os
import glob
import time
import shutil
import lcd
import cnn


class Recinto:
    camera1 = {}
    camera2 = {}
    ind_camera1 = {}
    ind_camera2 = {}
    empty1 = {}
    emtpy2 = {}
    open = {}
    close = {}
    lcd_line = {}
    stop = {}
    go = {}
    counter = 0
    thNut = 3000000
    empty_buffer_time = 0.4
    open_sleep_time = 0.4
    stop_motor = True

    def zero_pad(self,x, n):
        for i in range(1, 5):
            if x < 10 ** i:
                return (n - i) * '0' + str(x)

    def __init__(self, ind_camera1, ind_camera2, open, close,stop,go,lcd_line,thNut):
        self.thNut = thNut
        self.lcd_line = lcd_line
        self.counter = 0
        self.ind_camera1 = ind_camera1
        self.ind_camera2 = ind_camera2
        self.camera1 = cv2.VideoCapture(ind_camera1)
        self.camera1.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
        self.camera1.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
        self.camera2 = cv2.VideoCapture(ind_camera2)
        self.camera2.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
        self.camera2.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
        self.open = open
        self.close = close
        self.stop = stop
        self.go = go
        print("Inicializando cámaras "+str(ind_camera1)+' y '+str(ind_camera2))
        time.sleep(2)
        open()
        time.sleep(1)
        close()
        self.clear_buffer()
        s, empty1 = self.camera1.read()
        s, empty2 = self.camera2.read()
        th = 140
        empty_gray1 = cv2.cvtColor(empty1, cv2.COLOR_BGR2GRAY)
        trash, self.empty1 = cv2.threshold(empty_gray1, th, 255, cv2.THRESH_BINARY)
        empty_gray2 = cv2.cvtColor(empty2, cv2.COLOR_BGR2GRAY)
        trash, self.empty2 = cv2.threshold(empty_gray2, th, 255, cv2.THRESH_BINARY)

    def take_photos(self):
        th = 140
        s, img1 = self.camera1.read()
        s, img2 = self.camera2.read()
        img_gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        trash, img_BW1 = cv2.threshold(img_gray1, th, 255, cv2.THRESH_BINARY)
        img_gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        trash, img_BW2 = cv2.threshold(img_gray2, th, 255, cv2.THRESH_BINARY)

        diff1 = self.empty1 - img_BW1
        diff2 = self.empty2 - img_BW2
        if diff1.sum() > self.thNut or diff2.sum() > self.thNut:
            print(diff1.sum())
            print(diff1.sum())
            self.classify_nut()

    def clear_buffer(self):
        start = time.time()
        while time.time() - start < self.empty_buffer_time:
                self.camera1.read()
                self.camera2.read()

    def classify_nut(self):
        if self.stop_motor:
            self.stop()
        self.clear_buffer()
        s1, img1 = self.camera1.read()
        s2, img2 = self.camera2.read()
        self.open()
        cv2.imwrite('data/nuez'+str(self.ind_camera1)+'_' + self.zero_pad(self.counter, 6) + '.png', img1)
        cv2.imwrite('data/nuez'+str(self.ind_camera2)+'_' + self.zero_pad(self.counter, 6) + '.png', img2)
        time.sleep(self.open_sleep_time)
        self.close()
        self.clear_buffer()
        if self.stop_motor:
            self.go()
        self.counter += 1
        lcd.lcd_string("Nueces IZQ: " + str(self.counter), self.lcd_line)


