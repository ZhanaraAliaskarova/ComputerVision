import cv2
import numpy as np

img = cv2.imread(r"C:\github\Labs\Lab3\kokserek.jpg")
#convert to grayscale
imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', imgg)
cv2.waitKey(0)

ret, otsu = cv2.threshold(imgg,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('thresh', otsu)
cv2.waitKey(0)

kernel = np.ones((2,3),np.uint8)
erosion = cv2.erode(otsu,kernel,iterations = 1)
cv2.imwrite('erosion.jpg', erosion)
cv2.imshow('erosion', erosion)
cv2.waitKey(0)

#function allow to destroy all windows at any time
cv2.destroyAllWindows()
