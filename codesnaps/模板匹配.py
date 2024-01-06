import cv2 as cv
import numpy as np
header = cv.imread("../data/head-bottle.jpg")
boundary = cv.imread("../data/boundary2.jpg")
image = cv.imread("../data/half-bottle.jpg")


# 查看水位线匹配值
rv = cv.matchTemplate(image, boundary, cv.TM_SQDIFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(rv)
bh, bw = boundary.shape[0], boundary.shape[1]
topLeft = minLoc
bottomRight = (topLeft[0] + bw, topLeft[1]+bh)
cv.rectangle(image, topLeft, bottomRight, 255, 2)

# 查看瓶盖的匹配值
rv = cv.matchTemplate(image, header, cv.TM_SQDIFF_NORMED)
_, _, minLoc, _ = cv.minMaxLoc(rv)
hh, hw = header.shape[0], header.shape[1]
topLeft = minLoc
bottomRight = (topLeft[0] + hw, topLeft[1]+hh)
cv.rectangle(image, topLeft, bottomRight, 125, 2)

# 展示匹配结果
cv.imshow("image", image)
cv.waitKey(0)
cv.destroyAllWindows()
