import cv2 as cv
import numpy as np

def frameDiff(prevFrame, currFrame, nextFrame):
    diffFrames1 = cv.absdiff(nextFrame, currFrame)
    diffFrames2 = cv.absdiff(currFrame,prevFrame)
    return cv.bitwise_or(diffFrames1, diffFrames2)

def getFrame(cap):
    ret, frame = cap.read()
    frame = cv.resize(frame, None, fx=scalingFactor, fy = scalingFactor, interpolation=cv.INTER_AREA)    
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

if __name__=='__main__':
    cap = cv.VideoCapture(0)
    scalingFactor = 0.9
    prevFrame = getFrame(cap)    
    currFrame = getFrame(cap)    
    nextFrame = getFrame(cap)    

    while True:
        frameDifference = frameDiff(prevFrame, currFrame, nextFrame)
        value ,frameThreshold = cv.threshold(frameDifference, 0, 255, cv.THRESH_TRIANGLE)


        cv.imshow('res',frameDifference)
        cv.imshow('threshold',frameThreshold)

        prevFrame = currFrame
        currFrame = nextFrame
        nextFrame = getFrame(cap)

        key = cv.waitKey(5)
        if key == 27:
            break
    
    cv.destroyAllWindows()