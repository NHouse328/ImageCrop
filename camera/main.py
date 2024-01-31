# importing the python open cv library
import cv2

import PIL
from PIL.Image import *

# intialize the webcam and pass a constant which is 0
cam = cv2.VideoCapture(0)

# let's assume the number of images gotten is 0
img_counter = 0

# while loop
while True:
    # intializing the frame, ret
    ret, frame = cam.read()
    # if statement
    if not ret:
        print('failed to grab frame')
        break
    # the frame will show with the title of test
    cv2.imshow('test', frame)


# release the camera
cam.release()

# stops the camera window
cam.destoryAllWindows()