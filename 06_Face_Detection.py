### Imoort Libraries ###

import cv2
import numpy as np
import matplotlib.pyplot as plt

### Cascade Files
# Opencv comes with pre-trained cascadd files


### Face Detection

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")


def detect_face(img):

	face_img = img.copy()

	face_rectangle = face_cascade.detectMultiScale(face_img)

	for (x, y, w,h) in face_rectangle:
		# face_detected =cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255,255), 10)
		center = (x + w//2, y + h//2)
		frame = cv2.ellipse(face_img, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)


		eye_circle = face_cascade.detectMultiScale(frame)

		for (x2, y2, w2, h2) in eye_circle:
			eye_center = (x + x2 + w2//2, y + y2 + h2//2)

			radius = int(round((w2 + h2)*0.25))
			frame = cv2.circle(frame, eye_center, radius, (255, 0, 0 ), 4)


# def detect_eye(img):

# 	eye_img = img.copy()

# 	eye_circle = face_cascade.detectMultiScale(eye_img)

# 	for (x,y, w, h) in eye_circle:
# 		radius = int(round(w + h * 0.25))
# 		cv2.circle(eye_img, (x + y // 2, w + h // 2), radius, (255,0,0), 1)

# 	return eye_img


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