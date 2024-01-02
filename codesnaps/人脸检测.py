import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)
faceCascade = cv.CascadeClassifier("../data/haarcascade_frontalface_default.xml")

while True:
    succ, frame = video.read()
    frame = np.fliplr(frame)
    frame = np.ascontiguousarray(frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5))
    print("发现{0}个人脸".format(len(faces)))

    # 逐个标注人脸
    for (x, y, w, h) in faces:
        cv.circle(frame, (int((x+x+w)/2), int((y+y+h)/2)), int(w/2), (0, 255, 0), 2)
    cv.imshow("face cascade", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()