import cv2 as cv
import numpy as np

# Create an empty image
dizi = np.zeros((256, 256, 3), dtype='uint8')

# Fill the left third with a red gradient
for i in range(256):
    dizi[i, :85, 0] = 255 - i  # Red channel

# Fill the middle third with a green gradient
for i in range(256):
    dizi[i, 85:170, 1] = 255 - i  # Green channel

# Fill the right third with a blue gradient
for i in range(256):
    dizi[i, 170:, 2] = 255 - i  # Blue channel

cv.imshow("Gradient Image", dizi)
cv.waitKey(0)
cv.destroyAllWindows()