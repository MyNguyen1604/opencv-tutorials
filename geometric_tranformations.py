# Goal
# Learn to apply different geometric transformation to images like translation, rotation, affine transformation etc.
# OpenCV provides two transformation functions, cv.warpAffine() and cv.warpPerspective(). cv.warpAffine() takes a 2x3 transformation matrix while cv.warpPerspective()takes a 3x3 transformation matrix as input

# SCALING
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img = cv.imread('dog.jpg') #Possible with a color image
# res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
# #OR
# # height, width = img.shape[:2]
# # res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)

# cv.imshow('Original', img)
# cv.imshow('Scaling', res)


# TRANSLATION

# rows,cols = img.shape
# M = np.float32([[1,0,100],[0,1,50]]) #translate to position (x,y) = (100,50)
# # M must be a 2x3 matrix
# dst = cv.warpAffine(img,M,(cols,rows)) #(cols,rows) is the size of the output image
# # Third argument of the cv.warpAffine() function is the size of the output image, which should be in the form of **(width, height)**. Remember width = number of columns, and height = number of rows.
# # dst = cv.warpAffine(img,M,(300,300))
# cv.imshow('img',dst)

# ROTATION

# M = cv.getRotationMatrix2D((cols/2,rows/2),90,1) #((x_center,y_center),angle,scale): find the rotation matrix
# dst = cv.warpAffine(img,M,(cols,rows))

# cv.imshow('img',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# AFFINE TRANSFORMATION #Bien doi ma tran theo 3 diem tham chieu, tuc la bien mot ma tran voi cac diem tham chieu cua ma tran nay trung voi cac diem tham chieu tren ma tran moi
## ma tran moi la ma tran ket qua cua phep bien doi
# img = cv.imread('drawing.png')
# rows,cols,ch = img.shape
# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
# # In affine transformation, all parallel lines in the original image will still be parallel in the output image. To find the transformation matrix, we need three points from input image and their corresponding locations in output image
# # Then cv.getAffineTransform will create a 2x3 matrix which is to be passed to cv.warpAffine.
# M = cv.getAffineTransform(pts1,pts2)
# dst = cv.warpAffine(img,M,(cols,rows))
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()

# PERSPECTIVE TRANSFORMATION ## Co the dung de lay thong tin quan trong tren anh, Luu y, anh co the BI SCALE

# For perspective transformation, you need a 3x3 transformation matrix. 
# To find this transformation matrix, you need 4 points on the input image and corresponding points on the output image
# Among these 4 points, 3 of them should not be collinear
# img = cv.imread('sudoku.jpg')
img = cv.imread('test_perpective_transformation.jpg')
rows,cols = img.shape[:2]
# pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]]) #Four points in input image
# pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]]) #Four points in output image
pts1 = np.float32([[405,197],[758,197],[405,607],[758,607]]) #Four points in input image
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]]) #Four points in output image
M = cv.getPerspectiveTransform(pts1,pts2) #get the transformation matrix 3x3 for perspective transformation

dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
# "Computer Vision: Algorithms and Applications", Richard Szeliski