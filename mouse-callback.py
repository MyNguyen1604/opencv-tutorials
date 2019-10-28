import numpy as np
import cv2 as cv

# events = [i for i in dir(cv) if 'EVENT' in i]
# print( events )
# mouse callback function // Ham con
# def draw_circle(event,x,y,flags,param):
#     # if event == cv.EVENT_LBUTTONDBLCLK:
#     #     cv.circle(img,(x,y),100,(255,0,0),-1)
#     print cv.EVENT_LBUTTONDOWN
#     if event == cv.EVENT_LBUTTONDOWN:
#     	cv.circle(img,(x,y),100,(255,0,0),-1)

# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv.namedWindow('image')
# cv.setMouseCallback('image',draw_circle) #Set truoc cho image, khi trong vong while ham mouseCallBack luon chay
# while(1):
#     cv.imshow('image',img)
#     if cv.waitKey(20) & 0xFF == 27:
#         break

# cv.destroyAllWindows()

# Avanced Application
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
col = [0, 255, 0]
col2 = [0, 0, 255]
Ra = 1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,col,col2,Ra

    if event == cv.EVENT_LBUTTONDOWN: #Dieu kien bat dau ve
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE: #Thuc hien ve
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),col,-1)
            else:
                cv.circle(img,(x,y),Ra,col2,-1)
    elif event == cv.EVENT_LBUTTONUP: #Dieu kien ket thuc ve
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),col,-1)
        else:
            cv.circle(img,(x,y),Ra,col2,-1) #De co the ve mot diem tron khong can phai di chuyen chuot

def nothing(x):
    pass

img = np.zeros((512,512,3), np.uint8) #Tao mot anh den
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle) #Thiet lap ham draw_circle la mot ham mouseCallback, ham nay se thuc thi khi co su kien cua mouse xay ra

cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('Radius','image',1,100,nothing)
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    Ra = cv.getTrackbarPos('Radius','image')
    s = cv.getTrackbarPos(switch,'image')
    if s == 1:
    	if mode == True:
    		col = [b,g,r]
    	else: 
    		col2 = [b,g,r]
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv.destroyAllWindows()