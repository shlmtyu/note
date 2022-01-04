import numpy as np
import cv2

""" a = np.uint8(13) # 原始訊息
print('a=>', np.unpackbits(a))

x = np.uint8(111) # 加密⽤的鑰匙
print('x=>', np.unpackbits(x))

c = np.bitwise_xor(a, x) # 加密後的結果
print('c=>', np.unpackbits(c))
d = np.bitwise_xor(c, x) # 透過key再還原回來
print('d=>', np.unpackbits(d))
 """

pic=cv2.imread("picadd.jpg",-1)
key=np.random.randint(0,256,size=pic.shape,dtype=np.uint8)
encryption=cv2.bitwise_xor(pic,key)
decryption=cv2.bitwise_xor(encryption,key)
cv2.imshow("encryption",pic)
cv2.imshow("key",key)
cv2.imshow("encryption",encryption)
cv2.imshow("decryption",decryption)
cv2.waitKey()
cv2.destroyAllWindows()