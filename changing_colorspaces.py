# Goal
# In this tutorial, you will learn how to convert images from one color-space to another, like BGR2Gray, BGR2HSV etc.
# In addition to that, we will create an application which extracts a colored object in a video
# You will learn following functions : cv.cvtColor(), cv.inRange() etc.

# There are more than 150 color-space conversion methods available in OpenCV.
#Pay attention on BGR2Gray and BGR2HSV
# For BGR2Gray conversion we use the flags cv.COLOR_BGR2GRAY. Similarly for BGR2HSV, we use the flag cv.COLOR_BGR2HSV. To get other flags, just run following commands in your Python terminal :
# >>> import cv2 as cv
# >>> flags = [i for i in dir(cv) if i.startswith('COLOR_')]
# >>> print( flags )

# For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]. Different software use different scales. So if you are comparing OpenCV values with them, you need to normalize these ranges.

# Object Tracking

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    lower_green = np.array([50,50,50])
    upper_green = np.array([70,255,255])

    lower_red = np.array([0,100,100])
    upper_red = np.array([10,255,255])
    # Threshold the HSV image to get only blue colors
    mask_B = cv.inRange(hsv, lower_blue, upper_blue)
    mask_G = cv.inRange(hsv, lower_green, upper_green)
    mask_R = cv.inRange(hsv, lower_red, upper_red)
    # Bitwise-AND mask and original image
    mask = mask_B + mask_G + mask_R
    print frame.shape 
    res = cv.bitwise_and(frame,frame, mask= mask)
    # res_B = cv.bitwise_and(frame,frame, mask= mask_B)
    # res_G = cv.bitwise_and(frame,frame, mask= mask_G)
    # res_R = cv.bitwise_and(frame,frame, mask= mask_R)
    cv.imshow('frame',frame)
    cv.imshow('res', res)
    # cv.imshow('mask_B',mask_B)
    # cv.imshow('mask_G',mask_G)
    # cv.imshow('mask_R',mask_R)
    # cv.imshow('res_B',res_B)
    # cv.imshow('res_G',res_G)
    # cv.imshow('res_R',res_R)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
#How to find HSV values to track
# green = np.uint8([[[0, 255, 0]]])
# hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
# print hsv_green
#  Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively.