import cv2
import numpy as np

image = cv2.imread('me.jpg')
cv2.namedWindow('image')


def onScroll(value):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    v[:,:] = value
    roi = cv2.merge([h, s, v])
    art = cv2.cvtColor(roi, cv2.COLOR_HSV2BGR)
    cv2.imshow('image', art)

cv2.createTrackbar('ValBar', 'image', 0, 255, onScroll)
onScroll(100)
cv2.waitKey()
cv2.destroyAllWindows()