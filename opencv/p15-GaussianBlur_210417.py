import numpy as np
import cv2
img = cv2.imread("pic04.jpg")
cv2.imshow('normal', img)

noise = np.random.randint(0, 255, size = img.shape, dtype = np.uint8)
t, noise = cv2.threshold(noise, 240,255,cv2.THRESH_TOZERO)
o = cv2.add(img, noise)
cv2.imshow("noise", o)

r1 = cv2.blur(o,(5,5))
cv2.imshow("blur", r1)
r2 = cv2.GaussianBlur(o,(5,5), 0, 0)
cv2.imshow("GaussianBlur",r2)
r3 = cv2.medianBlur(o, 5)
cv2.imshow("medianBlur",r3)
r4 = cv2.bilateralFilter(o, 25, 100, 100)
cv2.imshow("bilateralFilter",r4)
cv2.waitKey()
cv2.destroyAllWindows()
