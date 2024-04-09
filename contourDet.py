from ctypes import resize
from statistics import mode
import numpy as np
import cv2 as cv

image = cv.imread('Fruits.jpg')

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

contours, hierarchy = cv.findContours(binary, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)

image = cv.drawContours(image, contours, -1, (0,255,0), thickness=2)

cv.imshow('imagbinary', binary)
cv.imshow('image', image)

cv.waitKey(0)
cv.destroyAllWindows()