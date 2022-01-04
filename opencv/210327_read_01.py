import cv2

pic = cv2.imread('testpic.jpeg')
#print(pic)

cv2.namedWindow('lesson-1')
cv2.imshow('sample', pic)
cv2.imwrite('output.png', pic)
cv2.waitKey()
cv2.destroyWindow('lession-1')
#cv2.destroyAllWindows()