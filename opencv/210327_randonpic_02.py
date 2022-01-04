import cv2
import numpy as np


#單通道，灰階
img=np.zeros((160,160),dtype=np.uint8)
cv2.imshow("one",img)

for i in range(160):
   for j in range(160):
       if np.random.rand() > 0.8:
           img[i, j] = 255

cv2.imshow("two", img)
cv2.waitKey()
cv2.destroyAllWindows()

#三通道，全彩
img=np.zeros((300,300,3),dtype=np.uint8)
img[:,0:100,0]=255
img[:,100:200,1]=255
img[:,200:300,2]=255
print("img=\n",img)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()

#
img=np.random.randint(0,256,size=[256,256,3],dtype=np.uint8)
print(img.item(10, 10, 0))
print(img.item(10, 10, 1))
print(img.item(10, 10, 2))
for i in range(100, 150):
   for j in range(100, 120):
       img.itemset((i, j, 0), 0)
       img.itemset((i, j, 1), 0)
       img.itemset((i, j, 2), 0)
cv2.imshow("demo",img)
cv2.waitKey()
cv2.destroyAllWindows()