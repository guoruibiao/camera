import cv2 as cv
import numpy as np

image = np.random.randint(0, 200, size=[600, 600], dtype=np.uint8)
image.itemset((100, 100), 255)
cv.imshow("uint8", image)

image = np.random.randint(0, 200, size=[600, 600, 3], dtype=np.uint8)
image.itemset((200, 200, 0), 255)
cv.imshow("RGB", image)


image = np.random.randint(0, 200, size=[600, 600, 4], dtype=np.uint8)
image.itemset((200, 200, 0), 255)
cv.imshow("ARGB", image)

cv.waitKey()
cv.destroyAllWindows()
