import cv2
import os

cam=cv2.VideoCapture(0)
cam.set(3,640) #width
cam.set(4,480) #height

face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input("\n Enter user id : ")

print("\n Initializing...")

count = 0
while(True):

	# Check if the webcam is opened correctly
	if not cam.isOpened():
		raise IOError("Cannot open webcam")  

	
	ret,img = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_detector.detectMultiScale(gray, 1.3, 5)


	for(x, y, w, h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		count+=1

		cv2.imwrite("Dataset/User." +str(face_id) + '.' +str(count) + ".jpg", gray[y:y+h,x:x+w])
		cv2.imshow('image',img)

		k = cv2.waitKey(10) & 0xff
		if k==27 or k== ord('a'):
			break
		elif count>=1:
			break


print("\n Exiting...")
cam.release()
cv2.destroyAllWindows()
