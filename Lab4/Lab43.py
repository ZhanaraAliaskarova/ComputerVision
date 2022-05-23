import cv2
import numpy as np

img = cv2.imread(r"./geometric.jpg")

width, height = 750, 350

# pixel points of 4 corners
pts1 = np.float32([[67,186],[755,10],[61,411],[739,214]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
result = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("img", img)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
