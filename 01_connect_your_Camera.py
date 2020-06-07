import cv2

# Take a video. 0 means the camera of my computer
cap = cv2.VideoCapture(0)


# Get the Width and Height of the Video Frame
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# print(width, height)


# Get The Writer with the Video name, formate, FPS, Width and Height
#	For Whndows --> *'DIVX'
#	For Linux or MacOs --> *'XVID'
output = cv2.VideoWriter("myvideo.mkv", cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))


# Get ready to do magic!

while True:
	ret, frame = cap.read()

	#Operations
	output.write(frame)

	#Show it

	# If you want a Gray Frame
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# cv2.imshow('frame', gray)

	cv2.imshow('frame', frame)
	# 27 == esc button. You can use any other button like ord('q')
	# if you try to close the window pressing the x youw'll get in trouble (^_^)
	if cv2.waitKey(5) & 0xFF == 27:
		break

#Never forget first to relese
#And then to destory
cap.release()
output.release()
cv2.destroyAllWindows()