import cv2

img = cv2.imread("D:/TuteDude/Module21/joker.jfif")

print("Dimensions of Original Image: ",img.shape)
scale = 50

width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
print("Dimensions of Reszied Image: ",resized.shape)

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
