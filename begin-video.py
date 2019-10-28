import numpy as np
import cv2 as cv

# // Capture video from camera
# cap = cv.VideoCapture(0)
# print cap.get(cv.CAP_PROP_FRAME_WIDTH)
# print cap.get(cv.CAP_PROP_FRAME_HEIGHT)
# ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,320)
# ret = ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,240)
# print cap.get(cv.CAP_PROP_FRAME_WIDTH)
# print cap.get(cv.CAP_PROP_FRAME_HEIGHT)
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv.imshow('frame',gray)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()

# // Playing video from file

# cap = cv.VideoCapture('video.mp4')
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # cv.imshow('frame',gray)
#     cv.imshow('frame',frame)
#     if cv.waitKey(25) & 0xFF == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()

# //Saving a video
cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'MJPG')
out = cv.VideoWriter('output.avi',fourcc, 15, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # frame = cv.flip(frame,0)
        # write the flipped frame
        out.write(frame)
        cv.imshow('frame',frame)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()