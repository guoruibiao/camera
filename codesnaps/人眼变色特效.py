import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)
faceCascade = cv.CascadeClassifier("../data/haarcascade_frontalface_default.xml")

while True:
    succ, frame = video.read()
    frame = np.fliplr(frame)
    frame = np.ascontiguousarray(frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    circles1 = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1,
                                100, param1=100, param2=30, minRadius=50, maxRadius=100)
    if circles1 is None:
        print("未找到人脸")
        break
    circles = circles1[0, :, :]  # 提取为二维
    circles = np.uint16(np.around(circles))  # 四舍五入，取整
    for i in circles[:]:
        cv.circle(frame, (i[0], i[1]), i[2], (255, 0, 0), 5)  # 画圆
        cv.circle(frame, (i[0], i[1]), 2, (255, 0, 255), 20)  # 画圆心
    cv.imshow("face cascade", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()