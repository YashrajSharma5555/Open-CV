
import numpy as np
import cv2 as cv

cap = cv.VideoCapture('random.mp4')
fps = cap.get(cv.CAP_PROP_FPS)

ret ,prevFrame = cap.read()
ret ,currFrame = cap.read()

while True:

    frameDiff = cv.absdiff(prevFrame, currFrame)
    gray = cv.cvtColor(frameDiff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)
    _, threshold = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    contours,hierarchy = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    frame = cv.drawContours(prevFrame.copy(), contours, -1, (0,255,0), 2)


    cv.imshow('image', frame)

    prevFrame = currFrame
    _,currFrame = cap.read()

    # key = cv.waitKey(int(1000/fps))
    key = cv.waitKey(1)
    if key == 27:
        break


cv.destroyAllWindows()
