#canny Edge Detection

#1 Noise reduction
#2 Intensity of the gradient of the image
#3 Non-maximum suppression
#4 Thersholding

import cv2
import numpy as np

img = cv2.imread("D:/TuteDude/Module21/joker.jfif")
resize = cv2.resize(img,(300,300))
min_thresh = 100
max_thresh = 200
#above 200 converted to white, below 100 converted to black

edges = cv2.Canny(resize,min_thresh,max_thresh)

cv2.imshow("edges",edges)
cv2.imshow("img",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
