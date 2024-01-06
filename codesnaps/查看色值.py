import cv2 as cv
import numpy as np

"""
../data/half-bottle.jpg
shape= (1344, 621, 3)
此处色值为： [128 116 112]
此处色值为： [175 142 127]
此处色值为： [154 127 117]
"""

# height, width, channels = image.shape
image = cv.imread("../data/half-bottle.jpg")
print("shape=", image.shape)
# hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
# 水位线以上部分
x, y, h, w = 310, 520, 20, 20
print("此处色值为：", image[y,x])
color = (255, 0, 0)
cv.rectangle(image, (x, y), (x+h, y+w), color, 2)

# 水位线
x, y, h, w = 310, 597, 20, 20
print("此处色值为：", image[y,x])
color = (0, 255, 0)
cv.rectangle(image, (x, y), (x+h, y+w), color, 2)

# 水位线以下部分
x, y, h, w = 310, 720, 20, 20
print("此处色值为：", image[y,x])
color = (0, 0, 255)
cv.rectangle(image, (x, y), (x+h, y+w), color, 2)

cv.imshow("image", image)
cv.waitKey(0)
cv.destroyAllWindows()