import cv2
import numpy as np
img = cv2.imread('me.jpg')
cv2.imshow('Original Image',img)

new_img = cv2.Canny(img, 0, 200)
cv2.imshow('new image',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
