import cv2
import numpy as np

img = cv2.imread("D:/TuteDude/Module21/joker.jfif")

thershold_value = 200 #if the color in image exceed 200 then it returs white

_,binary_thershold = cv2.threshold(img, thershold_value, 255, cv2.THRESH_BINARY)

cv2.imshow("binary",binary_thershold)
cv2.waitKey(0)
cv2.destroyAllWindows()
