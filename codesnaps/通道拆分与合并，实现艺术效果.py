import cv2 as cv

img = cv.imread("../data/water_bottle.jpg")
print(img.shape)
print(img.shape[:2])
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
h, s, v = cv.split(hsv)
v[:,:] = 255

merged = cv.merge([h, s, v])
cv.imshow("original", img)
cv.imshow("merged", merged)

cv.waitKey()
cv.destroyAllWindows()