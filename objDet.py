import cv2 as cv
import numpy as np

def frameDiff(prevFrame, currFrame, nextFrame):
    diffFrames1 = cv.absdiff(nextFrame, currFrame)
    diffFrames2 = cv.absdiff(currFrame,prevFrame)
    return cv.bitwise_and(diffFrames1, diffFrames2)


def getFrame(video):
    ret, frame = video.read()
    frame = cv.resize(frame, None, fx=scalingFactor, fy = scalingFactor, interpolation=cv.INTER_AREA)   
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

video = cv.VideoCapture('motion.mp4')
scalingFactor = 0.9
fps = video.get(cv.CAP_PROP_FPS)

prevFrame = getFrame(video)
currFrame = getFrame(video)
nextFrame = getFrame(video)

while True:


    frame = frameDiff(prevFrame, currFrame, nextFrame)



    cv.imshow('Motion Detection', frame)


    prevFrame = currFrame
    currFrame = nextFrame
    nextFrame = getFrame(video)


    key = cv.waitKey(int(1000/fps))

    if key == 27:
        break




cv.waitKey(0)
cv.destroyAllWindows()