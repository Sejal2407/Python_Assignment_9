import cv_2

img = cv2.imread("D:/TuteDude/Module21/joker.jfif",0) #argument 0 make the image in black and white

print("Dimensions of the image : ",img.shape)
#if the image is black and white it will return two value height and width, otherwise it will return 2 values ,one extra will be the rgb value

width = img.shape[1] #width remains same
height = 500
dim = (width, height)
resized = cv2.resize(img, dim)

cv2.imshow("window", resized)
cv2.imwrite("Newjoker.png",img)
cv2.waitKey(1000) #window stays awake all the time

cv2.destroyAllWindows()