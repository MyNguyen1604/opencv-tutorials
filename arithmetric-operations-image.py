import numpy as np 
import cv2 as cv 

# img1 = cv.imread('ml.png')[0:459, 0:500]
# img2 = cv.imread('opencv_logo.png')[0:459, 0:500]

# #Image Blending dst = alpha.img1 + beta.img2 + gramma

# dst = cv.addWeighted(img1,0.7,img2,0.3,0) #alpha = 0.7, beta = 0.3, gramma = 0 // Add two image co xet den ty trong giua chung

# cv.imshow('dst',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

#Bitwise Operations 

# Load two images
img1 = cv.imread('ml.png')
img2 = cv.imread('opencv_logo_black.jpg')[0:459,:]

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)


ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY) #Binary Thresholding (Nguong nhi phan 0 va maxValue)
#ret = 10 is thresh (nguong), 255 is the maxValue (when img2gray[x,y] > thresh, mask[x,y] = maxValue and otherwise), mask is the output image
mask_inv = cv.bitwise_not(mask)

# print img2gray[306,328]

# print mask 

# print mask_inv

# print ret
# # Now black-out the area of logo in ROI
# img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv) #(roi & roi) & mask_inv, 255 ~1, 0~0
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)

# print img1_bg
# print img2_fg

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg) #black + anycolor = anycolor
img1[0:rows, 0:cols ] = dst

cv.imshow('res',img1)
# cv.imshow('res.', mask)
# cv.imshow('res..', mask_inv)
# cv.imshow('res0',img2gray)
# cv.imshow('res',img2_fg)
# cv.imshow('res2',img1_bg)

cv.waitKey(0)
cv.destroyAllWindows()
