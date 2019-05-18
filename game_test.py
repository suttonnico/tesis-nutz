import pygame
import pygame.camera as cam
import time
cam.init()
cam0 = cam.Camera("/dev/video0",(640,480))
cam2 = cam.Camera("/dev/video2",(640,480))
cam4 = cam.Camera("/dev/video4",(640,480))
cam6 = cam.Camera("/dev/video6",(640,480))


cam0.start()
cam2.start()
cam4.start()
cam6.start()
start = time.time()
time.sleep(2)
down_time = 1
img0 = cam0.get_image()
time.sleep(down_time)
img2 = cam2.get_image()
time.sleep(down_time)
img4 = cam4.get_image()
time.sleep(down_time)
img6 = cam6.get_image()
time.sleep(down_time)

print(time.time()-start)
pygame.image.save(img0,"data/test3_0.jpg")
pygame.image.save(img2,"data/test3_2.jpg")
pygame.image.save(img4,"data/test3_4.jpg")
pygame.image.save(img6,"data/test3_6.jpg")

