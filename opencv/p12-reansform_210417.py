import numpy as np
import cv2

pCount = 0
points = np.ndarray((4, 2), dtype=np.float32)
#左上 右上 左下 右下 順序點
def onMouse(event, x, y, flags, params):
    global pCount   #全域變數
    if pCount >= 4: return
    if event == cv2.EVENT_LBUTTONDOWN:
        points[pCount] = [x, y]
        pCount += 1

book = cv2.imread('pic02.jpeg')
rows, cols = book.shape[:2]
cv2.namedWindow('book')
cv2.imshow('book', book)
cv2.setMouseCallback('book', onMouse)
cv2.waitKey()
print('points: ', points)

pts2 = np.float32([[0, 0], [700, 0], [0, 1400], [1500, 2000]]) 
M = cv2.getPerspectiveTransform(points,pts2) 
dst = cv2.warpPerspective(book, M, (700, 1400))
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyWindow('book')