import cv2 as cv

image = cv.imread("../data/water_bottle.jpg")
cv.imshow("original", image)
print("original: ", image[0:1, 0:1])

hls = cv.cvtColor(image, cv.COLOR_BGR2HLS)
cv.imshow("HLS", hls)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
print("gray: ", gray[0:1], gray.shape)

ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
cv.imshow("ycrcb", ycrcb)

cv.waitKey()
cv.destroyAllWindows()