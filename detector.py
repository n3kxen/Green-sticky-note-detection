import cv2 as cv
import numpy as np
from config import AREA_FROM, AREA_TO, E_RATIO, ANGLE_COUNT

def object_detection(img):

    mask = color_detection(img)

    contours = image_contour(mask)

    for i, cnt in enumerate(contours):
        area = cv.contourArea(cnt)
        if area >= AREA_FROM and area < AREA_TO:
            epsilon = E_RATIO*cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt,epsilon,True)
            if len(approx) >= ANGLE_COUNT:
                x,y,w,h = cv.boundingRect(cnt)
                rect = cv.rectangle(
                        img,
                        (x,y),
                        (x+w,y+h),
                        (0,255,0),
                        2)

                img = cv.putText(
                        rect, 
                        'square',
                        (x,y),
                        cv.FONT_HERSHEY_PLAIN,
                        3,
                        (0,255,0),
                        3,
                        cv.LINE_AA)
    return img



def image_contour(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    thresh = cv.adaptiveThreshold(
            img_gray,
            255,
            cv.ADAPTIVE_THRESH_MEAN_C,
            cv.THRESH_BINARY_INV,
            11,
            8)

    contours, hierarchy = cv.findContours(
            thresh, 
            cv.RETR_TREE,
            cv.CHAIN_APPROX_SIMPLE)

    return contours 

def color_detection(img):

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lower_red = np.array([51,80,80])
    upper_red = np.array([79,255,255])

    mask = cv.inRange(hsv, lower_red, upper_red)

    return cv.bitwise_and(img, img, mask= mask)


    
    
