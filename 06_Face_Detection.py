### Imoort Libraries ###

import cv2
import numpy as np
import matplotlib.pyplot as plt

### Cascade Files
# Opencv comes with pre-trained cascadd files


### Face Detection

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def detect_face(img):

	face_img = img.copy()

	face_rectangle = face_cascade.detectMultiScale(face_img)

	for (x, y, w,h) in face_rectangle:
		# cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 0, 0), 1)

		center = (x + w//2, y + h//2)
		cv2.ellipse(face_img, center, (w//2, h//2), 0, 0, 360, (255, 0, 0), 2)


	return face_img



### Face detection With Live Video

cap = cv2.VideoCapture(0)

while True:

	ret, frame = cap.read()

	face_img = detect_face(frame)

	# final = detect_eye(face_img)
	cv2.imshow("Face Detection Video", face_img)


	if cv2.waitKey(3) & 0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()