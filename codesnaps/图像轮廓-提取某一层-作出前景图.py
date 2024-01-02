import cv2 as cv
import numpy as np

img = cv.imread("../data/water_bottle.jpg")
cv.imshow("original", img)

# 查找轮廓必须在黑色背景上做，因此先滤波处理下
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 200, cv.THRESH_BINARY)
counters, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

mask = np.zeros(img.shape, dtype=np.uint8)
mask = cv.drawContours(mask, counters, -1, (255, 255, 255), -1)
cv.imshow("mask", mask)

loc = cv.bitwise_and(img, mask)
cv.imshow("location", loc)

cv.waitKey()
cv.destroyAllWindows()