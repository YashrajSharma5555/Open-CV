from unicodedata import name
import numpy as np
import cv2 as cv

def trackbar_callback(value):
    pass

cv.namedWindow("Trackbars")


cv.createTrackbar("Upper Hue", "Trackbars", 153, 180, trackbar_callback)
cv.createTrackbar("Upper Saturation", "Trackbars", 255, 255, trackbar_callback)
cv.createTrackbar("Upper Value", "Trackbars", 255, 255, trackbar_callback)
cv.createTrackbar("Lower Hue", "Trackbars", 64, 180, trackbar_callback)
cv.createTrackbar("Lower Saturation", "Trackbars", 72, 255, trackbar_callback)
cv.createTrackbar("Lower Value", "Trackbars", 49, 255, trackbar_callback)


def getFrame(cap, scalingFactor):
    ret, frame = cap.read()
    frame = cv.resize(frame, None, fx = scalingFactor, fy = scalingFactor , interpolation=cv.INTER_AREA)
    return frame


if __name__=='__main__':

    cap = cv.VideoCapture(0)
    scalingFactor = 0.9

    while True:

        frame = getFrame(cap, scalingFactor)

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)




        u_hue = cv.getTrackbarPos("Upper Hue", "Trackbars")
        u_saturation = cv.getTrackbarPos("Upper Saturation", "Trackbars")
        u_value = cv.getTrackbarPos("Upper Value", "Trackbars")
        l_hue = cv.getTrackbarPos("Lower Hue", "Trackbars")
        l_saturation = cv.getTrackbarPos("Lower Saturation", "Trackbars")
        l_value = cv.getTrackbarPos("Lower Value", "Trackbars")

        Upper_hsv = np.array([u_hue, u_saturation, u_value])
        Lower_hsv = np.array([l_hue, l_saturation, l_value])

        mask = cv.inRange(hsv, Lower_hsv, Upper_hsv)

        res = cv.bitwise_and(frame, frame, mask=mask)

        res = cv.medianBlur(res, 5)


        cv.imshow('mask',mask)
        cv.imshow('res',res)
        cv.imshow('frame',frame)

        cv.waitKey(1)



        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()
