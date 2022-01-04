#幾何轉換
#縮放
import numpy as np  #高y*寬x #python:寬x*高y 
import cv2

me = cv2.imread('me.jpg')
print(me.shape)

rows, cols = me.shape[0:2]
smallMe = cv2.resize(me, (int(cols*0.5), int(rows*0.9)) ) 
# 注意：
# dsize參數是tuple，所以外面還需要再一個括弧
# rows跟cols的位置要互換
print(smallMe.shape)
print(smallMe)
cv2.imshow('smallMe', smallMe)
biggerMe = cv2.resize(me, None, fx= 2, fy=1.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow('biggerMe', biggerMe)
cv2.waitKey()
cv2.destroyAllWindows()
