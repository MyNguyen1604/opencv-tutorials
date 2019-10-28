import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt

#Load and show image
img = cv.imread('fruit.jpg',1)

#Convert color RGB image to Gray image using the equation G = 0.299*R + 0.587*G + 0.114*B
row,col,channel = img.shape

g = np.zeros((row,col,1),np.float)
G = np.zeros((row,col,1),np.uint8)
# print g.dtype
rows = xrange(1,row,1)
cols = xrange(1,col,1)
for x in rows:
	for y in cols:
		g[x,y] = 0.299*img[x,y,2] + 0.587*img[x,y,1] + 0.114*img[x,y,0] #BGR in OpenCV
		G[x,y] = int(g[x,y])
# print g
# print G.dtype
img2 = img
G_func = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

#Display the R-G-B channels seperately
imgR = cv.imread('fruit.jpg',1)
imgG = cv.imread('fruit.jpg',1)
imgB = cv.imread('fruit.jpg',1)

# imgR = img
# imgG = img
# imgB = img #Khong thuc hien duoc nhu vay vi imgR, imgG va imgB la nhu nhau

# ##Create R image
imgR[:,:,1] = 0
imgR[:,:,0] = 0
# ##Create G image
imgG[:,:,2] = 0
imgG[:,:,0] = 0
# ##Create B image
imgB[:,:,2] = 0
imgB[:,:,1] = 0

cv.imshow('Fruit',img)
cv.imshow('Fruit Gray',G)
cv.imshow('Fruit Gray Using Function',G_func)
cv.imshow('R Channel Image',imgR)
cv.imshow('G Channel Image',imgG)
cv.imshow('B Channel Image',imgB)
print G_func.shape
# plt.subplot(231),plt.imshow(img,'gray'),plt.title('Fruit')
# plt.subplot(232),plt.imshow(G,'gray'),plt.title('Fruit Gray')
# plt.subplot(233),plt.imshow(G_func,'gray'),plt.title('Fruit Gray using Function cv.cvtColor')
# plt.subplot(234),plt.imshow(imgR,'gray'),plt.title('R Channel Image')
# plt.subplot(235),plt.imshow(imgG,'gray'),plt.title('G Channel Image')
# plt.subplot(236),plt.imshow(imgB,'gray'),plt.title('B Channel Image')
# plt.show()
# print img
# print imgR
# print imgG
# print imgB
# print img.shape
# print row
# print col

cv.waitKey(0)
cv.destroyAllWindows()