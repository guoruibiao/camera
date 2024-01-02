import cv2 as cv
import numpy as np

img = cv.imread("../data/water_bottle.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
ishow = img.copy()

ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
kernel = np.ones((3, 3), dtype=np.uint8)
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
cv.imshow("dist_transform", dist_transform)
ret, fore = cv.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
cv.imshow("fore", fore)

cv.waitKey()
cv.destroyAllWindows()