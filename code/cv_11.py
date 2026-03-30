import cv2
import numpy as np

img = cv2.imread("D:/TuteDude/Module21/joker.jfif")

resize = cv2.resize(img,(300,300))
d = 7
sigmacolor = 500
sigmaspace = 500

b = cv2.bilateralFilter(img,d,sigmacolor,sigmaspace)

cv2.imshow("original",resize)
cv2.imshow("bilateral",b)
cv2.waitKey(0)
cv2.destroyAllWindows()
