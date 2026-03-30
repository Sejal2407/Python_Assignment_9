import cv2

img = cv2.imread("D:/TuteDude/Module21/joker.jfif")
width = 300
height = 289
dim = (width, height)
resized = cv2.resize(img,dim)

print("Size of Image : ",img.size) # in bytes

cv2.imshow("original",resized)
flip = cv2.flip(resized,1) #Horizontal if argument is 1
cv2.imshow("Horizontal",flip)

cv2.imshow("original",resized)
flip2 = cv2.flip(resized,0) #Vertical if argument is 0
cv2.imshow("Vertical",flip2)

cv2.imshow("original",resized)
flip3 = cv2.flip(resized,-1) #vertical and horizontal both if argument is -1
cv2.imshow("Horizontal and Vertical",flip3)

cv2.waitKey(0)
cv2.destroyAllWindows()

