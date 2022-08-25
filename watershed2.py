
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure, color, io


img = cv2.imread(r"C:\Users\niman\Desktop\code\35_0gy_2h_p6.tif")

cells=img[:,:,0] 

pixels_to_um = 0.454 

ret1, thresh = cv2.threshold(cells, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel = np.ones((3,3),np.uint8)
invert = cv2.bitwise_not(ret1)
 
erosion = cv2.erode(invert, kernel,
                    iterations=1)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

from skimage.segmentation import clear_border
opening = clear_border(opening) 
plt.imshow(opening, cmap='gray') 

sure_bg = cv2.dilate(opening,kernel,iterations=10)
plt.imshow(sure_bg, cmap='gray') 
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
plt.imshow(dist_transform, cmap='gray') #Dist transformed img. 

print(dist_transform.max())
ret2, sure_fg = cv2.threshold(dist_transform,0.5*dist_transform.max(),255,0)
plt.imshow(sure_fg, cmap='gray')

sure_fg = np.uint8(sure_fg)  
unknown = cv2.subtract(sure_bg,sure_fg)
plt.imshow(unknown, cmap='gray')

ret3, markers = cv2.connectedComponents(sure_fg)
plt.imshow(markers)

markers = markers+10

markers[unknown==255] = 0
plt.imshow(markers, cmap='jet')  
markers = cv2.watershed(img,markers)


img[markers == -1] = [0,255,255]  

img2 = color.label2rgb(markers, bg_label=0)

plt.imshow(img2)
cv2.imshow('Overlay on original image', img)
cv2.imshow('Colored Grains', img2)
cv2.waitKey(0)
  
