#import os
import cv2
import numpy as np

#os.system("sudo modprobe 'bcm2835-v4l2'")
#os.system("cvlc 'v4l2:///dev/video0 --v4l2-width 1920 --v4l2-height 1080 --v4l2-chroma h264 --sout '#standard{access=http,mux=ts,dst=0.0.0.0:1$

cap = cv2.VideoCapture(1)
cap.isOpened()

while True:
 _, frame = cap.read()
 if not _: continue

 #laplician  = cv2.Laplacian(frame,cv2.CV_64F)
 sobelx = cv2.Sobel(frame,cv2.CV_64F, 1, 0, ksize=5)
 sobely = cv2.Sobel(frame,cv2.CV_64F, 0, 1,ksize=5)
 edges = cv2.Canny(frame, 250 ,350)

 cv2.imshow('original',frame)
# cv2.imshow('laplician',laplician)
 cv2.imshow('sobelx',sobelx)
 cv2.imshow('sobely',sobely)
 cv2.imshow('sobely',edges)
 k = cv2.waitKey(5) & 0xFF
 if k==27:
    break

 cap.release()
 cv2.destroyAllWindows()


