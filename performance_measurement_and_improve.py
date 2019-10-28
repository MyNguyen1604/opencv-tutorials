import cv2 as cv
import numpy as np 
import time
# Goal
# Measure the performance of code
# Some tips improve the performance of code
# cv.getTickCount(): call it before and after the function execution to get number of clock-cycles used to execute a function
# e1 = cv.getTickCount()
# # your code execution
# e2 = cv.getTickCount()
# time = (e2 - e1)/ cv.getTickFrequency()
# cv.getTickFrequancy()
# can use cv.useOptimized() to check if it is enabled/disabled and cv.setUseOptimized(True/False) to enable/disable, OpenCV runs the optimized code if it is enabled

img1 = cv.imread('dog.jpg')
e1 = cv.getTickCount()
# e1 = time.time()
for i in xrange(5,49,2):
    img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
# e2 = time.time()
t = (e2 - e1)/cv.getTickFrequency()
print( t )
# print( e2 - e1 )