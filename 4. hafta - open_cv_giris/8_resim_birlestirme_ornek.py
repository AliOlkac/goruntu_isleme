import cv2

# Load the images
resim1 = cv2.imread('resim/resim.bmp')
resim2 = cv2.imread('resim/manzara.jpg')
resim3 = cv2.imread('resim/resim.png')

# Resize images to the same dimensions
height, width = resim1.shape[:2]
resim2 = cv2.resize(resim2, (width, height))
resim3 = cv2.resize(resim3, (width, height))

# Ensure all images have the same type
resim1 = resim1.astype(resim2.dtype)
resim3 = resim3.astype(resim2.dtype)

# Concatenate the images horizontally
birlesik_resim = cv2.hconcat((resim1, resim2, resim3))

# Save the concatenated image
cv2.imwrite('resim/birlestirilmis_resim.jpg', birlesik_resim)