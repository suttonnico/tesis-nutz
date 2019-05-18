import pygame
import pygame.camera

pygame.camera.init()
cam0 = pygame.camera.Camera("/dev/video0",(640,480))
cam0.start()
img = cam0.get_image()
pygame.image.save(img,"data/test2_0.jpg")