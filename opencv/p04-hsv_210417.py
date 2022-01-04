import cv2
import numpy as np

img = cv2.imread('me.jpg')
cv2.imshow('img-1',img)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
minV = np.min(v).astype(np.float32)
maxV = np.max(v).astype(np.float32)
v[:,:] = 255*(v[:,:]-minV)//(maxV-minV)
print(np.min(v))
print(np.max(v))
newpic = cv2.merge([h, s,v.astype(np.uint8)])
newimg = cv2.cvtColor(newpic, cv2.COLOR_HSV2BGR)
cv2.imshow('img-2',newimg)
cv2.waitKey()
cv2.destroyAllWindows()

