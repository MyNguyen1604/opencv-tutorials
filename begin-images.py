import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('map.pgm',0)

# cv.namedWindow('image', cv.WINDOW_NORMAL)
# cv.imshow('image',img)
# k = cv.waitKey(0)
# if k == 27:
# 	cv.destroyAllWindows()
# elif k == ord('s'):
# 	cv.imwrite('dog2.jpg',img)
# 	cv.destroyAllWindows()
# img2 = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.imshow(img2)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

# face = img[20:100, 25:160]

# cv.namedWindow('face', cv.WINDOW_NORMAL)
# cv.imshow('face',face)

# cv.waitKey(0)
# cv.destroyAllWindows()
