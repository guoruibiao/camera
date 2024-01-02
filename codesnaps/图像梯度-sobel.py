import cv2 as cv

img = cv.imread("../data/water_bottle.jpg", cv.IMREAD_GRAYSCALE)
sobelx = cv.Sobel(img, 0, 1, 0)
cv.imshow("original", img)
cv.imshow("sobel", sobelx)


cv.waitKey()
cv.destroyAllWindows()