import cv2
import numpy as np

img = cv2.imread('image.tif')

img_blue = img.copy()

# set green and red channels to 0
img_blue[:, :, 1] = 0
img_blue[:, :, 2] = 0

#cv2.imshow('',img_blue)
#cv2.waitKey(0)

b, g, r = cv2.split(img)
kSize = 3
bBlur = cv2.blur(b, (kSize, kSize))
print(bBlur.shape)
test = np.array([])
gEdges = cv2.Laplacian(bBlur, cv2.CV_8UC1)
circles = cv2.HoughCircles(gEdges, cv2.HOUGH_GRADIENT, 40, 10, param1=50,param2=60,minRadius=2,maxRadius=15)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img_blue,(i[0],i[1]),i[2],(0,255,0),2)

cv2.imshow('detected circles',img_blue)
cv2.waitKey(0)
cv2.destroyAllWindows()


