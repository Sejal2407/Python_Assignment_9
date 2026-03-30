import cv2
import numpy as np

img = cv2.imread("D:/TuteDude/Module21/joker.jfif")

resize = cv2.resize(img,(100,100))

ksize = (7,7) #kernel size
sigmax = 0
sigmay = 0

blur = cv2.GaussianBlur(resize,ksize,0)
cv2.imshow("original",resize)
cv2.imshow("blur",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()