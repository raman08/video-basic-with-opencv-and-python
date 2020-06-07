# Import Modules
import cv2


# Open the cideo fram the previous lession
cap = cv2.VideoCapture('myvideo.mkv')

# In case we wrote the path wrong
if cap.isOpened() == False:
	print('Error! Check your file path...')


# Some magic!
while cap.isOpened():

	ret, frame = cap.read()

	if ret == True:
	# We wrote it with 30 FPS on previous lession
	# SO, we need a delay of 1/30 if we want to see it
	# Uncomment the line below if tou want to see it
	# time.sleep(1/20)


		# Show it
		cv2.imshow('frame', frame)

		# 27 == esc button. You can use any other button like ord('q')
		# if you try to close the window pressing the x youw'll get in trouble (^_^)
		if cv2.waitKey(15) & 0xFF == 27:
			break

#Never forget first to relese
#And then to destory
cap.release()
cv2.destroyAllWindows()