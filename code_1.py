# Python script for Edge detection using OpenCV in Python using Sobel edge detection and laplacian method 
import cv2 
import numpy as np 

#for Capturing the livestream video content from system camera
capt = cv2.VideoCapture(0) 

while(1): 

	_, frame = capt.read() 
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
	sobeledx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5) 
	sobeledy = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5) 
	laplacian = cv2.Laplacian(frame,cv2.CV_64F) 
	
	cv2.imshow('sobeledx',sobeledx) 
	cv2.imshow('sobeledy',sobeledy) 
	cv2.imshow('laplacian',laplacian) 
	k = cv2.waitKey(5) & 0xFF
	if k == 27: 
		break

cv2.destroyAllWindows() 
cap.release() 

