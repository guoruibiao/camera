import cv2 as cv
import numpy as np
"""
在 inRange 内，嘴硬坐标值为 255，否则为 0
"""
# frame = np.random.randint(0, 256, size=[200, 200], dtype=np.uint8)
# cv.imshow("image", frame)
#
# mask = cv.inRange(frame, 240, 255)
# cv.imshow("mask", mask)


image = cv.imread("../data/water_bottle.jpg")
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow("image", image)
cv.imshow("hsv", hsv)

# 指定蓝色值的范围
minBlue = np.array([110, 50, 50])
maxBlue = np.array([130, 255, 255])
mask = cv.inRange(hsv, minBlue, maxBlue)

# 锁定原图上的蓝色区域
blue = cv.bitwise_and(image, image, mask=mask)
cv.imshow("blue", blue)

cv.waitKey()
cv.destroyAllWindows()