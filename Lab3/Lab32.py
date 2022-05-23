import cv2

img = cv2.imread(r"C:\github\Labs\Lab3\labka.jpg")
#convert to grayscale
imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('binary', imgg)
cv2.waitKey(0)

ret, otsu = cv2.threshold(imgg,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('labka', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()



