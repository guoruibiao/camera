import cv2 as cv
import numpy as np

header = cv.imread("./data/head-bottle.jpg")
boundary = cv.imread("./data/boundary2.jpg")

def detect(image, header, boundary):
    # 查看水位线的位置
    rv = cv.matchTemplate(image, boundary, cv.TM_SQDIFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(rv)
    bh, bw = boundary.shape[0], boundary.shape[1]
    topLeft = minLoc
    bottomRight = (topLeft[0] + bw, topLeft[1] + bh)
    cv.rectangle(image, topLeft, bottomRight, 255, 2)

    # 查看瓶盖的匹配值
    rv = cv.matchTemplate(image, header, cv.TM_SQDIFF_NORMED)
    _, _, minLoc, _ = cv.minMaxLoc(rv)
    hh, hw = header.shape[0], header.shape[1]
    topLeft = minLoc
    bottomRight = (topLeft[0] + hw, topLeft[1] + hh)
    cv.rectangle(image, topLeft, bottomRight, 125, 2)

    return


cap = cv.VideoCapture(0)
while True:
    ok, frame = cap.read()
    if not cap.isOpened() or not ok:
        break
    frame = np.fliplr(frame)
    frame = np.ascontiguousarray(frame)

    # 策略一：评估水位线移动信息
    detect(frame, header, boundary)
    # 策略二：评估相对位置移动信息

    if cv.waitKey(10) & 0xFF == ord('q'):
        break
    cv.imshow("Camera", frame)
# 释放资源
cap.release()
cv.destroyAllWindows()