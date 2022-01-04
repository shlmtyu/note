import cv2
import numpy as np

def doNothing(x):
	pass

size = 300
s = np.full((size, size), 255, dtype=np.uint8)
v = np.full((size, size), 255, dtype=np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('HueBar', 'image', 0, 180, doNothing)
cv2.setTrackbarPos('HueBar','image', 0)
#cv2.imshow('image', image)
while True:
hueBar = cv2.getTrackbarPos('HueBar','image')
h = np.full((size, size), hueBar, dtype=np.uint8)
roi = cv2.merge([h, s, v])
art = cv2.cvtColor(roi, cv2.COLOR_HSV2BGR)
cv2.imshow('image', art)
key = cv2.waitKey(100)
if key > -1:
	break

cv2.destroyAllWindows()
""" 
image = cv2.imread('me.jpg')
def doNothing(x): pass

cv2.namedWindow('image')
cv2.createTrackbar('HueMin', 'image', 0, 180, doNothing)
cv2.setTrackbarPos('HueMin','image', 0)
cv2.createTrackbar('HueMax', 'image', 0, 180, doNothing)
cv2.setTrackbarPos('HueMax','image', 180)
cv2.createTrackbar('SatMin', 'image', 0, 255, doNothing)
cv2.setTrackbarPos('SatMin','image', 0)
cv2.createTrackbar('SatMax', 'image', 0, 255, doNothing)
cv2.setTrackbarPos('SatMax','image', 255)
while True:
    minHue = cv2.getTrackbarPos('HueMin','image')
    maxHue = cv2.getTrackbarPos('HueMax','image')
    minSat = cv2.getTrackbarPos('SatMin','image')
    maxSat = cv2.getTrackbarPos('SatMax','image')
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    hueMask = cv2.inRange(h, minHue, maxHue)
    print(hueMask)
    satMask = cv2.inRange(s, minSat, maxSat)
    mask = hueMask & satMask
    roi = cv2.bitwise_and(image, image, mask= mask)
    cv2.imshow('image', roi)
    key = cv2.waitKey(100)
    if key > -1:
        break
cv2.destroyAllWindows() """
