#設定值(或叫門檻值、閥值) 處理(Threshold)
import cv2
import numpy as np

img = cv2.imread('pic07.jpg', 0)
""" #t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
#t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
#t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
print("t=", t)
cv2.imshow("rst", rst) """

""" print('cv2.THRESH_BINARY:', cv2.THRESH_BINARY)
print('cv2.THRESH_OTSU:', cv2.THRESH_OTSU)
t1,thd = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#t1,thd = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
#t1,thd = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#t1,thd = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
#t1,thd = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
t2,otsu = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#t2,otsu = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#t2,otsu = cv2.threshold(img,0,255,cv2.THRESH_TRUNC+cv2.THRESH_OTSU)
#t2,otsu = cv2.threshold(img,0,255,cv2.cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)
cv2.imshow("img",img)
cv2.imshow("thd",thd)
cv2.imshow("otsu",otsu)
print('t1:', t1)
print('t2:', t2) """


h, w = img.shape[:2]
testimg = cv2.resize(img, (w//2, h//2))
t1, thd = cv2.threshold(testimg, 127, 255, cv2.THRESH_BINARY) 
athdMEAN = cv2.adaptiveThreshold(testimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3) 
athdGAUS = cv2.adaptiveThreshold(testimg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3)

cv2.imshow("img",testimg)
cv2.imshow("thd",thd)
cv2.imshow("athdMEAN",athdMEAN)
cv2.imshow("athdGAUS",athdGAUS)

cv2.waitKey()
cv2.destroyAllWindows()
