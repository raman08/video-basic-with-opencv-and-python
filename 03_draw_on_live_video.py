# Import Libraries
import cv2

# Take a video. 0 means camera of my computer
cap = cv2.VideoCapture(0)


# Get the Width amd Height of the Video Frame
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))



# Top Left Corner
# We divide with // the Width and Height of the frame
# in order to get an Integer as a result
x = 0 #width // 2
y = 0 #height // 2


# Rectangle Width and Height
# 1/4 of the Actual Video Screen
w = width // 3
h = height // 3


# Bottom Right Corner == x + w, y + h


# It's a kind of Magic!
while True:
	ret, frame = cap.read()

	# Rectangle Frame
	cv2.rectangle(frame, (x, y), (x + w, y + h), color = (234, 231, 123), thickness = 1 )

	#Show it

	cv2.imshow('frame', frame)
	# 27 == esc button. You can use any other button like ord('q')
	# if you try to close the window pressing the x youw'll get in trouble (^_^)
	if cv2.waitKey(5) & 0xFF == 27:
		break

#Never forget first to relese
#And then to destory
cap.release()
cv2.destroyAllWindows()