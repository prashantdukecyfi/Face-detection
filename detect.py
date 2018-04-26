import cv2
import numpy as np
cap = cv2.VideoCapture(-1) #Camera started, change parameter to 0 or 1 if -1 doesn't work

face_cascade = = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Cascade data loaded here

while (True) :
	ret,img = cap.read() #Loads one frame of video into variable img
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converts coloured image into grayscale

	faces = face_cascade.detectMultiScale(gray, 1.3, 5) #Detects faces present in the given frame

	for (x,y,w,h) in faces: #Draws rectangle around the detected face
	    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]
	    print ("face detected")
		
	cv2.imshow('video',img) #Outputs the video frame by frame
	
	if (cv2.waitKey(100) & 0xFF == ord('q')) : #Exits the infinite loop on pressing 'q'
		break
cap.release()
cv2.destroyAllWindows
