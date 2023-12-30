# coding: utf8
import cv2
import numpy as np

frame = np.zeros((1024, 1024), dtype=np.uint8)
cv2.imshow("image", frame)

for i in range(1024):
    frame[i, i] = int("{}{}".format(i, i)) % 255
cv2.imshow("image2", frame)
cv2.waitKey()
cv2.destroyAllWindows()