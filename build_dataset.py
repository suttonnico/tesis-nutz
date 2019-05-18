import cv2
import i2c_module as i2c
import glob
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

device_paths = glob.glob('/dev/video*')

# Connect to each camera initially
camera_a_path = device_paths[0]
camera_a_camera = cv2.VideoCapture(camera_a_path)
camera_b_path = device_paths[1]
camera_b_camera = cv2.VideoCapture(camera_b_path)