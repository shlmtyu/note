import numpy as np
import cv2

""" img = cv2.imread("pic01.jpg")
cv2.imshow('pic01', img)
#h, w = img.shape
noise = np.random.randint(0, 255, size = img.shape, dtype = np.uint8)
t, noise = cv2.threshold(noise, 240,255,cv2.THRESH_TOZERO)
O = cv2.add(img, noise)


R = cv2.blur(O, (5, 5))
cv2.imshow('noise', O)
cv2.imshow("result", R) """

""" o=cv2.imread("me.jpg")
r=cv2.blur(o,(5,5))
cv2.imshow('noise', o)
cv2.imshow("result", r) """


o=cv2.imread("picadd.jpg")
r=cv2.boxFilter(o,-1,(5,5),normalize=1)
cv2.imshow("original",o)
cv2.imshow("result2",r)

cv2.waitKey()
cv2.destroyAllWindows()
