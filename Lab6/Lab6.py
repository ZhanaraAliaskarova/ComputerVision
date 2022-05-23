import cv2
#Upload and Convert image to Grayscale
img = cv2.imread("ball.jpg", cv2.IMREAD_GRAYSCALE)
#Change the size of image(make smaller)
img = cv2.resize(img, (0,0), fx = 0.5, fy=0.5)
#SIFT realization
SIFT = cv2.xfeatures2d.SIFT_create()
keyS = SIFT.detect(img, None)
imgS = cv2.drawKeypoints(img, keyS, None)
#FAST realization
fast = cv2.FastFeatureDetector_create()
keyF = fast.detect(img,None)
imgF = cv2.drawKeypoints(img, keyF, None)

cv2.imshow("SIFT", imgS)
cv2.imshow("FAST", imgF)

cv2.waitKey(0)
cv2.destroyAllWindows()