import cv2
import i2c_module as i2c
import glob
import time
i2c.stop()
i2c.openA1()
time.sleep(0.4)
i2c.closeA1()
i2c.closeA2()
i2c.closeB1()
i2c.closeB2()

def zero_pad(x,n):
    for i in range(1,5):
        if x < 10 ** i:
            return (n-i)*'0'+str(x)


"""
nut_dir = 'data/'
class camera_man:
    i = 0
    def __init__(self,i):
        self.i = i
    def shoot(self):
        s, img_0 = cam_0.read()
        s, img_1 = cam_1.read()
        s, img_2 = cam_2.read()
        s, img_3 = cam_3.read()

        cv2.imwrite('data/recinto1_L/nuez_' + zero_pad(self.i, 6) + '.png', img_1)
        cv2.imwrite('data/recinto1_R/nuez_' + zero_pad(self.i, 6) + '.png', img_2)
        self.i = self.i +1

"""

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

empty0 = cv2.imread('data/empty/empty0.png')
empty2 = cv2.imread('data/empty/empty2.png')
empty4 = cv2.imread('data/empty/empty4.png')
empty6 = cv2.imread('data/empty/empty6.png')

th = 140

empty_gray0 = cv2.cvtColor(empty0, cv2.COLOR_BGR2GRAY)
trash,empty_BW0 = cv2.threshold(empty_gray0, th, 255, cv2.THRESH_BINARY)

empty_gray2 = cv2.cvtColor(empty2, cv2.COLOR_BGR2GRAY)
trash,empty_BW2 = cv2.threshold(empty_gray2, th, 255, cv2.THRESH_BINARY)

empty_gray4 = cv2.cvtColor(empty4, cv2.COLOR_BGR2GRAY)
trash,empty_BW4 = cv2.threshold(empty_gray4, th, 255, cv2.THRESH_BINARY)

empty_gray6 = cv2.cvtColor(empty6, cv2.COLOR_BGR2GRAY)
trash,empty_BW6 = cv2.threshold(empty_gray6, th, 255, cv2.THRESH_BINARY)
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
i2c.go()
i = 100
j = 100
while 1:
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

    diff0 = empty_BW0 - img_BW0
    diff2 = empty_BW2 - img_BW2
    diff4 = empty_BW4 - img_BW4
    diff6 = empty_BW6 - img_BW6
    thr = 1500000
    #print("diff0"+str(diff0.sum()))
    #print("diff2"+str(diff2.sum()))
    #print("diff4"+str(diff4.sum()))
    #print("diff6"+str(diff6.sum()))
    if diff0.sum() > thr or diff2.sum() > thr or diff4.sum() > thr or diff6.sum() > thr:
        print('foto0 :' + str(diff0.sum()))
        print('foto2 :' + str(diff2.sum()))
        print('foto4 :' + str(diff4.sum()))
        print('foto6 :' + str(diff6.sum()))
        print(zero_pad(i, 6))


       # i2c.stop()
        i2c.openA1()
        time.sleep(0.4)

        cv2.imwrite('data/nuez0_' + zero_pad(i, 6) + '.png', img0)
        cv2.imwrite('data/nuez2_' + zero_pad(i, 6) + '.png', img2)
        cv2.imwrite('data/nuez4_' + zero_pad(i, 6) + '.png', img4)
        cv2.imwrite('data/nuez6_' + zero_pad(i, 6) + '.png', img6)
        start = time.time()
        i2c.closeA1()

        while time.time()-start < 0.4:
            s0, img0 = camera_0.read()
            s2, img2 = camera_2.read()
            s4, img4 = camera_4.read()
            s6, img6 = camera_6.read()
        i = i+1
        i2c.closeA1()

       # i2c.go()
        """
        if diff4.sum() > thr or diff6.sum() > thr:  # or diff4.sum() > thr or diff6.sum() > thr:
            print('foto0 :' + str(diff0.sum()))
            print('foto2 :' + str(diff2.sum()))
            print('foto4 :' + str(diff4.sum()))
            print('foto6 :' + str(diff6.sum()))
            print(zero_pad(j, 6))

            i2c.stop()
            i2c.openB1()
            time.sleep(0.4)
           # cv2.imwrite('data/nuez0_' + zero_pad(i, 6) + '.png', img0)
          #  cv2.imwrite('data/nuez2_' + zero_pad(i, 6) + '.png', img2)
            cv2.imwrite('data/nuez4_' + zero_pad(j, 6) + '.png', img4)
            cv2.imwrite('data/nuez6_' + zero_pad(j, 6) + '.png', img6)
            start = time.time()
            i2c.closeA1()

            while time.time() - start < 1:
        #        s0, img0 = camera_0.read()
         #       s2, img2 = camera_2.read()
                s4, img4 = camera_4.read()
                s6, img6 = camera_6.read()
            j = j + 1
            i2c.closeB1()

            i2c.go()
            """

exit()