import pygame
import pygame.camera

pygame.camera.init()
pygame.camera.list_camera() #Camera detected or not
cam0 = pygame.camera.Camera("/dev/video0",(640,480))
cam0.start()
img = cam0.get_image()
pygame.image.save(img,"test2_0.jpg")