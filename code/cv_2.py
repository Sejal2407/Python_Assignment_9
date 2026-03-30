'''
1)Erosion
Remove the pixels on the foreground objects
cv2.erode()

2)Dilation
Adds Pixels
cv2.dilate()

3)Opening
Erosion Followed by dilation
cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

4)Closing
DilationFollowed by Erosion
cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

5) Morphological Gradient
Difference Between Dilation and Erosion
cv2.morpohologyEx(img,cv2.MORPH_GRADIENT,kernel)

6)Top Hat
Difference Between Input Image and Opening of image
cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

7)Black Hat
Difference Between Closing Image and Opening of image
cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

What is kernel ?
Chaning the value
CONVOLUTION : When the kernel is applied to every pixel in the image one by one to produce the final image

DATA TYPE OF IMAGE
uint : most used one
Signed,unsigned,floating point
Unsigned -> No negative
Signed -> Negative and Positive
If image -> 8 bit unsigned, it is displayed as it is
If image -> 16-bit unsignest/32-bit unsigned pixel -> divided by 256, range[0,255]
If image -> 32-bit floating point, pixel -> multiplied by 256, range[0,1]
'''

import cv2
import numpy as np

img = cv2.imread("D:/TuteDude/Module21/joker.jfif")
width = 300
height = 289
dim = (width, height)
resized = cv2.resize(img,dim)

kernel = np.ones((3,3),dtype = 'uint8')

# erosion = cv2.erode(resized,kernel,iterations = 1)
# dilation = cv2.dilate(resized,kernel,iterations = 1)
# opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE,kernel)
# gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
top_hat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
black_hat =cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("Original",img)
# cv2.imshow("Erosion",erosion)
# cv2.imshow("Dilation",dilation)
# cv2.imshow("Opening",opening)
# cv2.imshow("Closing",closing)
# cv2.imshow("Gradient",gradient)
cv2.imshow("Top Hat",top_hat)
cv2.imshow("Black Hat",black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()


'''
| Operation   | Formula                  | What it Does              | Real Life Example              |
|-------------|--------------------------|---------------------------|--------------------------------|
| Erosion     | -                        | Shrinks shapes            | Sandpaper thinning a shape     |
| Dilation    | -                        | Expands shapes            | Fattening/thickening a shape   |
| Opening     | Erosion → Dilation       | Removes bright noise      | Cleaning dust off surface      |
| Closing     | Dilation → Erosion       | Fills dark holes/gaps     | Filling cracks in a wall       |
| Gradient    | Dilation - Erosion       | Detects edges/boundary    | Tracing outline of a drawing   |
| Top Hat     | Original - Opening       | Finds bright spots        | Finding freckles on a face     |
| Black Hat   | Closing - Original       | Finds dark spots          | Dark spots on bright surface   |
'''
