import size_classification
import cv2

img1 = cv2.imread('test/data/nuez0_000000.png')
print(img1)
img2 = cv2.imread('test/data/nuez6_000000.png')
empty1 = cv2.imread('test/data/empty0.png')
empty2 = cv2.imread('test/data/empty6.png')

size1 = size_classification.findRadius(img1, empty1)
size2 = size_classification.findRadius(img2, empty2)
print("pixeles camara 1:" + str(size1))
print("pixeles camara 2:" + str(size2))
print("Diametro: " + str(size_classification.sizes2rad(size1, size2, 120)))
