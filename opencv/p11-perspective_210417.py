#透視
import numpy as np
import cv2

me = cv2.imread('pic01.jpg')
print(me.shape)

rows, cols = me.shape[:2]
print(rows,cols)

pts1 = np.float32([[100, 100], [500, 100], [100, 500], [500, 500]])
pts2 = np.float32([[200, 200], [400, 200], [100, 500], [500, 500]]) 

M = cv2.getPerspectiveTransform(pts1,pts2) 
#注意矩陣大小跟之前的不一樣
dst = cv2.warpPerspective(me, M, (cols,rows))

cv2.imshow("img",me)
cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()
