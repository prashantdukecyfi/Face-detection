import cv2
import numpy as np
cap = cv2.VideoCapture(0)
capx = cv2.VideoCapture(1)
cap.set(3, 320);
cap.set(4, 240);
capx.set(3, 320);
capx.set(4, 240);
while (True) :
	ret,img = cap.read()
	_ , imgx = capx.read()
	cv2.imshow('img1',img)
	cv2.imshow('img2',imgx)
	if (cv2.waitKey(100) & 0xFF == ord('q')) :
		break
cap.release()
capx.release()
cv2.destroyAllWindows



