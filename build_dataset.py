import cv2
import i2c_module as i2c
import glob
import time
i2c.stop()
i2c.closeA1()
i2c.closeA2()

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

time.sleep(20)
s0, img_0 = camera_0.read()
s2, img_2 = camera_2.read()
s4, img_4 = camera_4.read()
s6, img_6 = camera_6.read()
time.sleep(0.5)

s0, img_0 = camera_0.read()
s2, img_2 = camera_2.read()
s4, img_4 = camera_4.read()
s6, img_6 = camera_6.read()
time.sleep(0.5)

#s0, img_0 = camera_0.read()
#s2, img_2 = camera_2.read()
s4, img_4 = camera_4.read()
#s6, img_6 = camera_6.read()
time.sleep(0.5)

#s6, img_6 = camera_6.read()
#time.sleep(0.1)
#s0, img_0 = camera_0.read()
#s2, img_2 = camera_2.read()
#time.sleep(1)
#s4, img_4 = camera_4.read()
#time.sleep(1)
#s6, img_6 = camera_6.read()


cv2.imwrite('data/test2_0.jpg', img_0)
cv2.imwrite('data/test2_2.jpg', img_2)
cv2.imwrite('data/test2_4.jpg', img_4)
cv2.imwrite('data/test2_6.jpg', img_6)

exit()
device_paths = glob.glob('/dev/video*')
# Connect to each camera initially
camera_AR_path = '/dev/video0'
camera_AR0 = cv2.VideoCapture(camera_AR_path)

camera_AR_path = '/dev/video2'
camera_AR2 = cv2.VideoCapture(camera_AR_path)

camera_AR_path = '/dev/video4'
camera_AR4 = cv2.VideoCapture(camera_AR_path)

camera_AR_path = '/dev/video6'
camera_AR6 = cv2.VideoCapture(camera_AR_path)

s, img_0 = camera_AR0.read()
s, img_2 = camera_AR2.read()
s, img_4 = camera_AR4.read()
s, img_6 = camera_AR6.read()


time.sleep(0.1)


s, img_0 = camera_AR0.read()
s, img_2 = camera_AR2.read()
s, img_4 = camera_AR4.read()
s, img_6 = camera_AR6.read()

time.sleep(0.1)


s, img_0 = camera_AR0.read()
s, img_2 = camera_AR2.read()
s, img_4 = camera_AR4.read()
s, img_6 = camera_AR6.read()

cv2.imwrite('data/test_0.png', img_0)
cv2.imwrite('data/test_2.png', img_2)
cv2.imwrite('data/test_4.png', img_4)
cv2.imwrite('data/test_6.png', img_6)
