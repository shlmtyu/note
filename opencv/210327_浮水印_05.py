import cv2
import numpy as np
tree = cv2.imread("pic04.jpg",0)
tree=cv2.resize(tree,(400,300))
watermark = cv2.imread("background.jpg",0)
watermark=cv2.resize(watermark,(400,300))
watermark[watermark > 0] = 1
h,w = tree.shape
#== 隱藏過程 ==
t254 = np.ones((h,w), dtype=np.uint8) * 254
tree2 = cv2.bitwise_and(tree, t254)
e = cv2.bitwise_or(tree2, watermark)
#== 還原過程 ==
t1 = np.ones((h,w),dtype=np.uint8)
wm = cv2.bitwise_and(e,t1)
cv2.imshow("tree",tree)
cv2.imshow("watermark",watermark * 255)
cv2.imshow("output",e)
cv2.imshow("wm",wm * 255)
cv2.waitKey()
cv2.destroyAllWindows()