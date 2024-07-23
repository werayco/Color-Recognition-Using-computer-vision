import cv2 as cv
import numpy as np
import matplotlib.image as imf
import matplotlib.pyplot as plt

# this secton helps with understanding the HSV color channel and it also helps picking the right color for the project

def onChange(x): # the callback function for the trackbar
    pass

cv.namedWindow("frame01")
cv.createTrackbar("b","frame01",0,179,onChange)
cv.createTrackbar("g","frame01",175,255,onChange)
cv.createTrackbar("r","frame01",175,255,onChange)
blank = np.zeros((300,300,3),np.uint8)


while True:
    b = cv.getTrackbarPos("b","frame01")
    g = cv.getTrackbarPos("g","frame01")
    r = cv.getTrackbarPos("r","frame01")

    blank[:] = b,g,r
    hsv = cv.cvtColor(blank,cv.COLOR_BGR2HSV)
    cv.imshow("frame01",hsv)
    if cv.waitKey(1) & 0xFF == ord("d"):
        break