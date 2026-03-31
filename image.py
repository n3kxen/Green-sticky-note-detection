import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('square.jpg')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

thresh1 = cv.adaptiveThreshold(img_gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)

contours, hierarchy = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for i, cnt in enumerate(contours):
    area = cv.contourArea(cnt)
    if area >= 90000:
        epsilon = 0.008 * cv.arcLength(cnt,True)
        approx = cv.approxPolyDP(cnt,epsilon,True)
        if len(approx) >= 4 and len(approx) < 6:
            print(i)
            img_rgb = cv.drawContours(img_rgb, contours, 
                                       i, (0,255,0), 10)




plt.imshow(img_rgb)
plt.show()
