import cv2

video = cv2.VideoCapture("D:/TuteDude/Module21/trial.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

output = cv2.VideoWriter('Output.mp4', fourcc,60.31,(2160,3840))
while video.isOpened():
    ret,frame = video.read()
    if ret:
        output.write(frame)
        cv2.imshow('frame',frame)

        if cv2.waitKey(10) == ord('s'):
            break
    else:
        break

cv2.destroyAllWindows()