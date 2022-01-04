#旋轉
import numpy as np
import cv2

me = cv2.imread('me.jpg')
print(me.shape)

height,width = me.shape[:2]
M = cv2.getRotationMatrix2D((width/2,height/2), 45, 0.6)
print("M:", M)
rotate=cv2.warpAffine(me,M,(width,height))
cv2.imshow("original",me)
cv2.imshow("rotation",rotate)
cv2.waitKey()
cv2.destroyAllWindows()
