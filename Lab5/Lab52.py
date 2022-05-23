import cv2

img = cv2.imread("ball.jpg", 100)

blur = cv2.GaussianBlur(img,(5,5),2)

laplacian = cv2.Laplacian(blur,cv2.CV_64F)

lap = laplacian / laplacian.max()

cv2.imshow("ballOriginal", img)
cv2.imshow("Gaussianblur", blur)
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)