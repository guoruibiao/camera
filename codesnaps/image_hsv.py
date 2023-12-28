# coding: utf8
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while True:
    succ, frame = cap.read()
    if not succ:
        break
    # 左右镜像调换
    frame = np.fliplr(frame)

    # 转为 hsv 空间
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower, upper = np.array([16,32,88]), np.array([99,255,255])
    mask = cv.inRange(hsv, lowerb=lower, upperb=upper)
    dst = cv.bitwise_and(frame, frame, mask=mask)

    # 展示照片
    # cv.imshow("Camera", frame)
    cv.imshow("mask", dst)


    # 按下 'q' 键退出循环
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头对象和关闭窗口
cap.release()
cv.destroyAllWindows()