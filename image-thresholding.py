# Goal
# In this tutorial, you will learn Simple thresholding, Adaptive thresholding, Otsu's thresholding etc.
# You will learn these functions cv.threshold, cv.adaptiveThreshold etc.







# #Simple Thresholding: cv.threshhold()

# Use a global value as threshold value (a threshold value is used for all pixels)
# If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black)
# Image inserted in cv.thresholdl() function should be a grayscale image
# Two outputs are obtained. First one is a retval. Second output is our thresholded image.
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img = cv.imread('dog.jpg',0)
# ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY) #Img is a grayscale image, 127 is threshold value, 255 is the value to be given if the pixel value is more than threshold value
# ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV) #Lon hon 127 se gan pixel gia tri 0, nguoc lai gan gia tri 255 (nguoc voi cv.THRESH_BINARY)
# ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC) #Lon hon 127 se gan pixel do la 127, nguoc lai giu nguyen gia tri pixel
# ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO) #Lon hon 127 se giu nguyen gia tri pixel, nguoc lai gan pixel gia tri 0
# ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV) #Lon hon 127 se gan pixel gia tri 0, nguoc lai giu nguyen gia tri pixel

# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# for i in xrange(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()











## Adaptive threshholding (nguong thich nghi) ---- LOCAL THRESHHOLDING
# The conditions where image has different lighting conditions in different areas --> adaptive thresholding
# the algorithm calculate the threshold for a small regions of the image
# So we get different thresholds for different regions of the same image and it gives us better results for images with varying illumination (chieu sang khac nhau)_ Mot noi thi qua toi, toi va mot noi thi qua sang, sang

# img = cv.imread('sudoku.jpg',0)
# img = cv.medianBlur(img,5) #Blurs an image using the median filter with 5x5 aperture; Each channel of a multi-channel image is processed independently
# ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
# 			cv.THRESH_BINARY,11,2)
# # https://docs.opencv.org/3.4.1/d7/d1b/group__imgproc__misc.html#ga72b913f352e4a1b1b397736707afcde3
# # https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html?highlight=threshold
# th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
# 			cv.THRESH_BINARY,11,2)  #2 is a constant subtracted from the mean or weighted mean. That mean, when we find T from blocksize x blocksize, the T will get new value this is T - C. Here, T = T - 2
# #C is found from Trying

# titles = ['Original Image', 'Global Thresholding (v = 127)',
#             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]
# for i in xrange(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()












## Otsu's binarization
# For images which are not bimodal, binarization wont be accurate
# In simple words, bimodal image is an image whose histogram has two peaks
# it automatically calculates a threshold value from image histogram for a bimodal image
# the algorithm finds the optimal threshold value and returns you as the second output, retVal
# If Otsu thresholding is not used, retVal is same as the threshold value you used

# img = cv.imread('noisy2.png',0)
# # global thresholding
# ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

# # Otsu's thresholding
# ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# # Otsu's thresholding after Gaussian filtering
# blur = cv.GaussianBlur(img,(5,5),0)# filtered image with a 5x5 gaussian kernel to remove the noise
# ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU) #Otsu algorithm automaticaly canculate thresholding value, so can pass thresh value in function is zero

# # plot all the images and their histograms
# images = [img, 0, th1,
#           img, 0, th2,
#           blur, 0, th3]
# titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
#           'Original Noisy Image','Histogram',"Otsu's Thresholding",
#           'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
# for i in xrange(3):
#     plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
#     plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])

#     plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)#images[].revel() sap xep cac phan tu cua ma tran thanh mot hang duy nhat, 256 la so cot gia tri cua histagram
#     plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])

#     plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
#     plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
# plt.show()
## How can otsu's binarian work
## find normalized_histogram, and its cumulative distribution function
# img = cv.imread('noisy2.png',0)
# blur = cv.GaussianBlur(img,(5,5),0)

# hist = cv.calcHist([blur],[0],None,[256],[0,256])
# hist_norm = hist.ravel()/hist.max()
# Q = hist_norm.cumsum()

# bins = np.arange(256)

# fn_min = np.inf
# thresh = -1

# for i in xrange(1,256):
#     p1,p2 = np.hsplit(hist_norm,[i]) # probabilities
#     q1,q2 = Q[i],Q[255]-Q[i] # cum sum of classes
#     b1,b2 = np.hsplit(bins,[i]) # weights
#     # finding means and variances
#     m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
#     v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
#     # calculates the minimization function
#     fn = v1*q1 + v2*q2
#     if fn < fn_min:
#         fn_min = fn
#         thresh = i
# # find otsu's threshold value with OpenCV function
# ret, otsu = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# print( "{} {}".format(thresh,ret) )

#-------------------------Active----------------------------------#
img = cv.imread('mypic.jpg',0)
blur = cv.GaussianBlur(img,(5,5),0)

# ret,thresh = cv.threshold(blur,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)

# th = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_MEAN_C,\
# 			cv.THRESH_BINARY,11,2)
# th2 = cv.adaptiveThreshold(th,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
# 			cv.THRESH_BINARY,11,2) 

th2 = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
			cv.THRESH_BINARY,11,3) ##cv.ADAPTIVE_THRESH_GAUSSIAN_C is Threshholding method, cv.THRESH_BINARY is Threshholding type

# plt.subplot(1,3,1), plt.imshow(blur,'gray')
# plt.title('Blur'), plt.xticks([]), plt.yticks([])	

# plt.subplot(1,3,2), plt.hist(blur.ravel(), 256)
# plt.title('Histagram'), plt.xticks([]), plt.yticks([])

# plt.subplot(1,3,3), plt.imshow(thresh,'gray')
# plt.title('Thresholding'), plt.xticks([]), plt.yticks([])

plt.plot(), plt.imshow(th2,'gray')
plt.title('Thresholding'), plt.xticks([]), plt.yticks([])

plt.show()