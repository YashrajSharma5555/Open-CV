import numpy as np
import cv2

ones = np.zeros((300,300,3), dtype = np.uint8)

image1 = np.array(ones, dtype = np.uint8)

cv2.circle(image1, (150,150), 150, (255,255,255), -1)

img = cv2.imread('nature.jpg')
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

image2 = cv2.resize(img, (300, 300))

result = cv2.bitwise_and(image1,image2)

cv2.imshow('result',result)
# cv2.imshow('result',image1)


cv2.waitKey(0)
cv2.destroyAllWindows()