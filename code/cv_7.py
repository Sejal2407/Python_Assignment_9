import cv2
import numpy as np

img = cv2.imread("D:/TuteDude/Module21/joker.jfif")

row = img.shape[1]
col = img.shape[0]

counter = (col/2,row/2)
angle = 90

r = cv2.getRotationMatrix2D(counter,angle,1)

rotate = cv2.warpAffine(img,r,(col,row))
cv2.imshow("img",rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()