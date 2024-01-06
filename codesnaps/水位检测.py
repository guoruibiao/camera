import cv2 as cv
import numpy as np

image = cv.imread("../data/half-bottle.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
orgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
oshow = orgb.copy()
lines = cv.HoughLines(edges, 1, np.pi/180, 140)
for line in lines:
    rho, theta = line[0]
    a, b = np.cos(theta), np.sin(theta)
    x0, y0 = a*rho, b*rho
    x1, y1, x2, y2 = int(x0+1000*(-b)), int(y0+1000*a), int(x0-1000*(-b)), int(y0-1000*a)
    cv.line(orgb, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv.imshow("image", orgb)
cv.waitKey(0)
cv.destroyAllWindows()
import sys
sys.exit(0)









hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
print("hsv.shape", hsv.shape)
print("水位线以上：", hsv[520, 310])
print("水位线：",    hsv[597, 310])
print("水位线以下：", hsv[720, 310])
# 使用灰度值阈值挑出目标区域
lower_blue = np.array([100, 65, 160])
upper_blue = np.array([110, 100, 190])
mask = cv.inRange(hsv, lower_blue, upper_blue)
cv.imshow("mask", mask)

# 去除噪点
kernel = np.ones((5,5), dtype=np.uint8)
mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

# 查找轮廓
contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print("counters.length=", len(contours))
total_area = image.shape[0] * image.shape[1]
for contour in contours:
    area = cv.contourArea(contour)
    if area > total_area * 0.5: # 水位低于总面积的50%
        print("水位低")
    else:
        print("水位正常")
cv.drawContours(image, contours, -1, (0, 255, 0), 2)
cv.imshow("image", image)
cv.waitKey(0)
cv.destroyAllWindows()