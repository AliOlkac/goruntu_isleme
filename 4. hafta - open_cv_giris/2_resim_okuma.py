import cv2 as cv

resim = cv.imread("resim/manzara.jpg")


print(resim)
print(resim.shape)
print(resim.ndim)

cv.imshow("manzara", resim)
cv.waitKey(0)