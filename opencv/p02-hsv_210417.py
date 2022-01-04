import cv2
import numpy as np

image = cv2.imread('me.jpg')

cv2.namedWindow('image')
cv2.createTrackbar('ValBar', 'image', 0, 100, lambda x: None)
cv2.setTrackbarPos('ValBar','image', 100)
while True:
ValBar = cv2.getTrackbarPos('ValBar','image')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
v[:,:] = v[:,:] * (ValBar/100)
roi = cv2.merge([h, s, v.astype(np.uint8)])
art = cv2.cvtColor(roi, cv2.COLOR_HSV2BGR)
cv2.imshow('image', art)
key = cv2.waitKey(100)
if key > -1:
break

cv2.destroyAllWindows()
