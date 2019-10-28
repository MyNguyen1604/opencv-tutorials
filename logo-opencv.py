import numpy as np
import cv2 as cv

img = np.zeros((512,1512,3),np.uint8)

cv.ellipse(img,(200,195),(50,50),90,45,315,(0,0,255),30)
cv.ellipse(img,(125,325),(50,50),-30,45,315,(0,255,0),30)
cv.ellipse(img,(275,325),(50,50),-90,45,315,(255,0,0),30)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(350,350), font, 8,(255,255,255),2,cv.LINE_AA)

cv.imshow('Logo-OpenCV',img)
cv.waitKey(0)
cv.destroyAllWindows()
