#平移 放大 縮小
import numpy as np
import cv2

me = cv2.imread('me.jpg')
print(me.shape)

#位移
rows, cols = me.shape[0:2] 
M = np.float32([[1, 0, 100], [0, 1, 100]])  
move = cv2.warpAffine(me,M,(cols,rows))
cv2.imshow('move', move)
#縮放
M = np.float32([[0.8, 0, -20], [0, 3, -20]])    #x縮0.8,y放大3倍
new1 = cv2.warpAffine(me,M,(cols,rows))
cv2.imshow('new1', new1)
#原圖(x,y) => (y,x)
M = np.float32([[0, 1, 0], [1, 0, 0]])
new2 = cv2.warpAffine(me,M,(rows,cols))
cv2.imshow('new2', new2)

#原圖(x,y) => 左右翻轉(-x,y) 
M = np.float32([[-1, 0, cols], [0, 1, 0]])
new2 = cv2.warpAffine(me,M,(rows,cols))
cv2.imshow('new3', new2)

#原圖(x,y) => 上下翻轉(x,-y)
M = np.float32([[1, 0, 0], [0, -1, rows]])
new2 = cv2.warpAffine(me,M,(rows,cols))
cv2.imshow('new4', new2)
cv2.waitKey()
cv2.destroyAllWindows()
