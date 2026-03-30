import cv2

video = cv2.VideoCapture("D:/TuteDude/Module21/trial.mp4")

while video.isOpened():
    _, frame = video.read()
    frame= cv2.resize(frame,(500,700))
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()