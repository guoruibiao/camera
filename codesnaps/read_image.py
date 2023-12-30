import cv2
import numpy

image = cv2.imread("../data/water_bottle.jpg")
print(image.shape)
print(image[12][34])
cv2.imshow("Blue passport", image[:,:,0])
cv2.imshow("Green passport", image[:,:,1])
cv2.imshow("Red passport", image[:,:,2])
cv2.waitKey()
cv2.destroyAllWindows()