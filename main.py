import cv2 as cv
import numpy as np
from config import FRAME_WIDTH, FRAME_HEIGHT
from detector import object_detection, image_contour, color_detection


cap = cv.VideoCapture(0)
cap.set(3, FRAME_WIDTH) 
cap.set(4, FRAME_HEIGHT)
cap.set(10,150)

while cap.isOpened():
    success, img = cap.read()
    if not success:
        print("Cant read video stream")
    
    #cv.imshow("Result", object_detection(img))
    
    cv.imshow("result", object_detection(img))

    if cv.waitKey(1) & 0xFF == ord('q'):
        break




