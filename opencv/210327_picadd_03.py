import numpy as np
import cv2

lena = cv2.imread('picadd.jpg', -1)
print(lena.shape)
cv2.imshow('lena', lena)

image1 = np.random.randint(0, 256, size=lena.shape, dtype=np.uint8)
image2 = cv2.add(lena, image1)
image3 = cv2.addWeighted(lena, 0.5, image1, 0.5, 100)
cv2.imshow('lena2', image2)
cv2.imshow('lena3', image3)
cv2.waitKey()
cv2.destroyAllWindows()