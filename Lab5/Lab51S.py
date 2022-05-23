import cv2
import numpy as np
#Sobel edge detection
img = cv2.imread("ball.jpg", cv2.IMREAD_GRAYSCALE)

Sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
Sobely = cv2.Sobel(img,cv2.CV_64F,0,1)

cv2.imwrite("Sobel.jpg",Sobelx+Sobely)

