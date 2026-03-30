import cv2
import numpy as np

img = cv2.imread("D:/TuteDude/Module21/joker.jfif")

resize = cv2.resize(img,(200,200))
kernel = 3

blur = cv2.medianBlur(img,kernel)

cv2.imshow("original",resize)
cv2.imshow("blurred",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()