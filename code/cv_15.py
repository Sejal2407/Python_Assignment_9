import cv2

video = cv2.VideoCapture(0) # 0 means your web cam
while video.isOpened():
    _,frame = video.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
