import cv2
import numpy as np

img = cv2.imread("D:/TuteDude/Module21/joker.jfif",cv2.IMREAD_COLOR)
# img = np.zeros(shape = [600,800,3])
cv2.line(img,(0,0),(20,20),(255,0,0),2)

cv2.rectangle(img,(10,10),(50,50),(255,0,0),2)

cv2.circle(img,(10,75),70,(255,0,255),3)

pts_polygon = np.array([[50,40],[10,30],[50,5],[50,30]],np.int32)

cv2.polylines(img,[pts_polygon],True,(0,255,255),3)

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,"hello",(50,50),font,2,(0,0,255),2,cv2.LINE_AA)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()