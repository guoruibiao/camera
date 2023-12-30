import cv2 as cv

img = cv.imread("../data/water_bottle.jpg")
blur55 = cv.blur(img, ksize=(5, 5))
cv.imshow("blur_5_5", blur55)

blur1010 = cv.blur(img, ksize=(10, 10))
cv.imshow("blur_10_10", blur1010)


blur2020 = cv.blur(img, ksize=(20, 20))
cv.imshow("blur_20_20", blur2020)


blur30_30 = cv.blur(img, ksize=(30, 30))
cv.imshow("blur_30_30", blur30_30)



cv.waitKey()
cv.destroyAllWindows()