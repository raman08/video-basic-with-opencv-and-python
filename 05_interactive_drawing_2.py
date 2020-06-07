# Import Library
import cv2

# Callback Function for mouse, Circle
def draw_circle(event, x, y, flags, params):

	global center, clicked

	# Get the mouse Click Down & Up
	#and Track the Center
	if event == cv2.EVENT_LBUTTONDOWN:
		center = (x, y)
		clicked = False

	if event == cv2.EVENT_LBUTTONUP:
		clicked = True

# Zero Drawing of the Circle
center = (0, 0)
clicked = False

# Take a video
cap = cv2.VideoCapture(0)


# Create a Named Window for the Connections
cv2.namedWindow('Test')


# Set a Mouse Callback
cv2.setMouseCallback('Test', draw_circle)


# Time for magic
while True:

	# Capture the frame
	ret, frame = cap.read()

	# Check if Clicked is True
	if clicked:

		# Draw a Circle on the Frame
		cv2.circle(frame, center=center, radius=50, color=(255, 0, 234), thickness=3)


	# Display the frame
	cv2.imshow('Testing', frame)

	# 27 == esc button. You can use any other button like ord('q')
	# if you try to close the window pressing the x youw'll get in trouble (^_^)
	if cv2.waitKey(5) & 0xFF == 27:
		break

#Never forget first to relese
#And then to destory
cap.release()
cv2.destroyAllWindows()