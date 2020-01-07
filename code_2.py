# OpenCV program to perform Edge detection in real time import libraries of python OpenCV where its functionality resides 
import cv2 
import numpy as np 

capt = cv2.VideoCapture(0) 

while(1): 

	ret, frame = capt.read() 
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
	lower_red_range = np.array([30,150,50]) 
	upper_red_range = np.array([255,255,180]) 
	mask = cv2.inRange(hsv, lower_red_range, upper_red_range) 
	res = cv2.bitwise_and(frame,frame, mask= mask) 
	cv2.imshow('Original Camera',frame) 
	edges_detected = cv2.Canny(frame,100,200) 
	cv2.imshow('Edges Detected',edges_detected) 

	k = cv2.waitKey(5) & 0xFF
	if k == 27: 
		break

capt.release() 
cv2.destroyAllWindows() 

