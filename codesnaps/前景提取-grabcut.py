import cv2 as cv
import numpy as np

img = cv.imread("../data/water_bottle.jpg")
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
mask = np.zeros(img.shape[:2], dtype=np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (50, 50, 400, 500)
cv.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
ogc = img*mask2[:,:,np.newaxis]
ogc = cv.cvtColor(ogc, cv.COLOR_BGR2RGB)

# plt.subplot(121)
# plt.axis('off')
# plt.imshow(rgb)
# plt.subplot(122)
# plt.axis('off')
# plt.imshow(ogc)

cv.waitKey()
cv.destroyAllWindows()