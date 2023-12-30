import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

while True:
    ok, frame = video.read()
    if not ok:
        break

    frame = np.fliplr(frame)
    frame = np.ascontiguousarray(frame)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)
    v[:,:] = np.random.randint(0, 256)
    cv.merge([h, s, v])
    cv.imshow("Camera", hsv)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()

