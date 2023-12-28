# coding: utf8
import os
import time
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# 预置首帧作为对照
previous_frame = None
es = cv.getStructuringElement(cv.MORPH_ELLIPSE, (9, 4))
last_alert_time = 0


while True:
    succ, frame = cap.read()
    if not succ:
        break
    # 左右镜像调换
    frame = np.fliplr(frame)
    frame = np.ascontiguousarray(frame)
    gray_lwpCV = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_lwpCV = cv.GaussianBlur(gray_lwpCV, (21, 21), 0)

    # 检测是否移动
    if previous_frame is None:
        previous_frame = gray_lwpCV
        continue
    # absdiff 检测两幅图的绝对差值
    img_delta = cv.absdiff(previous_frame, gray_lwpCV)
    thresh = cv.threshold(img_delta, 10, 255, cv.THRESH_BINARY)[1]
    thresh = cv.dilate(thresh, es, iterations=2)
    # findContours 检测物体轮廓（寻找轮廓的图像，轮廓的检索模式，轮廓的近似方法）
    counters, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in counters:
        if cv.contourArea(c) < 1500:
            continue
        else:
            (x, y, w, h) = cv.boundingRect(c)
            # cv.rectangle(img, pt1, pt2, color, thickness, lineType, shift )
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv.putText(frame, "检测到轮廓", (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # TODO 做一些提醒
            # os.system("""osascript -e 'display notification "content" with title "title"'""")
            current_alert_time = int(time.time())
            if current_alert_time - last_alert_time >= 30:
                print("this is an alert...")
                last_alert_time = current_alert_time

    # 为上一帧赋值，用于后续检测
    previous_frame = gray_lwpCV

    # 展示照片
    cv.imshow("Camera", frame)


    # 按下 'q' 键退出循环
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    # time.sleep(10)

# 释放摄像头对象和关闭窗口
cap.release()
cv.destroyAllWindows()