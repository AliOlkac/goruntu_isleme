"""
Bir satranç tahtası oluşturunuz...
"""
import cv2 as cv
import numpy as np

satranc=np.zeros((800,800),dtype="uint8")
print(satranc.shape)


for i in range(0,8):
    for j in range(0,8):
        if (i+j)%2==0:
            satranc[i*100:i*100+100,j*100:j*100+100]=255

cv.imshow("satranc",satranc)
cv.waitKey(0)
































# dizi = np.zeros((800, 800), dtype="uint8")
#
#
#
#
# for i in range(0, 8):
#     for s in range(0, 8):
#         if (i+s)%2 == 0:
#             dizi[i*100:i*100+100, s*100:s*100+100] = 255
#
#
#
# cv.imshow("1", dizi)
# cv.waitKey(0)