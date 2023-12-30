import cv2 as cv
image = cv.imread("../data/water_bottle.jpg")
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
h, s, v = cv.split(hsv)
# 色调值范围
minHue, maxHue = 5, 170
hueMask = cv.inRange(h, minHue, maxHue)
# 饱和度范围
minSat, maxSat = 25, 166
satMask = cv.inRange(s, minSat, maxSat)

mask = hueMask & satMask
roi = cv.bitwise_and(image, image, mask=mask)
cv.imshow("image", image)
cv.imshow("ROI", roi)



cv.waitKey()
cv.destroyAllWindows()