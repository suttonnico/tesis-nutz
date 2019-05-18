import pygame
import pygame.camera
import time
pygame.camera.init()
cam0 = pygame.camera.Camera("/dev/video0",(640,480))
cam2 = pygame.camera.Camera("/dev/video2",(640,480))
cam4 = pygame.camera.Camera("/dev/video4",(640,480))
cam6 = pygame.camera.Camera("/dev/video6",(640,480))


cam0.start()
cam2.start()
cam4.start()
cam6.start()
start = time.time()
img0 = cam0.get_image()
time.sleep(0.01)
img2 = cam2.get_image()
time.sleep(0.01)
img4 = cam4.get_image()
time.sleep(0.01)
img6 = cam6.get_image()
time.sleep(0.01)

img0 = cam0.get_image()
time.sleep(0.01)
img2 = cam2.get_image()
time.sleep(0.01)
img4 = cam4.get_image()
time.sleep(0.01)
img6 = cam6.get_image()
time.sleep(0.01)

img0 = cam0.get_image()
time.sleep(0.01)
img2 = cam2.get_image()
time.sleep(0.01)
img4 = cam4.get_image()
time.sleep(0.01)
img6 = cam6.get_image()
time.sleep(0.01)

print(time.time()-start)
pygame.image.save(img0,"data/test2_0.jpg")
pygame.image.save(img2,"data/test2_2.jpg")
pygame.image.save(img4,"data/test2_4.jpg")
pygame.image.save(img6,"data/test2_6.jpg")

