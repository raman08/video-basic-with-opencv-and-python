# Import Library
import cv2

# Callback Function for mouse, Rectangle
def draw_rectangle(event, x, y, flags, params):

	# write your global params.
	# Check the project Computer Vision - Image Basics with OpenCV and Python
	# to get an idea how you can do it
	# pt1, pt2, top_left_clicked, bottom_right_clicked
	global pt1, pt2, top_left_clicked, bottom_right_clicked

	# Create an event for left Button Down and sddigned it to event
	if event == cv2.EVENT_LBUTTONDOWN:

	# Reset your Rectangle
		if top_left_clicked == True and bottom_right_clicked == True:

			# Give 0 values to pt1 & pt2
			pt1 = (0, 0)
			pt2 = (0, 0)

			# Give False value to your Trackes
			top_left_clicked = False
			bottom_right_clicked = False


	# Check the top_left_clicked if it's false
	if top_left_clicked == False:
		pt1 = (x, y)
		top_left_clicked = True


	# Check the top_left_clicked if it's false
	if bottom_right_clicked == False:
		pt1 = (x, y)
		bottom_right_clicked = True

# pt1, pt2 Global Variables
pt1 = (0, 0)
pt2 = (20, 20)

#Tracks are false
top_left_clicked = False
bottom_right_clicked = False


# Take a video
cap = cv2.VideoCapture(0)


# Create a Named Window for the Connections
cv2.namedWindow('Test')


# Set a Mouse Callback
cv2.setMouseCallback('Test', draw_rectangle)


# Time for magic
while True:

	# Capture the frame
	ret, frame = cap.read()

	# Based on global Variables Draw the Frame
	if top_left_clicked == True and bottom_right_clicked == True:
		cv2.circle(frame, center=pt1, radius=10, color = (255, 0, 255), thickness = 3)

		# Draw a Rectangle in Frame
	if top_left_clicked == True and bottom_right_clicked == True:
		cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 1)

	# Show the frame
	cv2.imshow('frame', frame)

	# 27 == esc button. You can use any other button like ord('q')
	# if you try to close the window pressing the x youw'll get in trouble (^_^)
	if cv2.waitKey(5) & 0xFF == 27:
		break

#Never forget first to relese
#And then to destory
cap.release()
cv2.destroyAllWindows()