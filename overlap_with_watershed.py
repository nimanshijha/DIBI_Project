import os.path

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r'C:\Users\niman\Desktop\code\35_0gy_2h_p6.tif')
orig_img = img.copy()

# set green and red channels to 0
img[:, :, 0] = 0
img[:, :, 2] = 0

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel = np.ones((3,3),np.uint8)
closing = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE, kernel, iterations = 1)

dist = cv2.distanceTransform(closing, cv2.DIST_L2, 3)

ret, dist1 = cv2.threshold(dist, 0.01*dist.max(), 255, 0)


markers = np.zeros(dist.shape, dtype=np.int32)
dist_8u = dist1.astype('uint8')



#markers = cv2.watershed(img, markers)
#img[markers == -1] = [0,0,255]
plt.imshow(dist_8u)
plt.show()