import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r'C:\Users\niman\Desktop\code\35_8gy_24h_p6.tif')


orig_image = image.copy()

# set green and red channels to 0
image[:, :, 1] = 0
image[:, :, 2] = 0

kernel = np.ones((5,5),np.uint8)
image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
# keep a copy of the original image
# convert to RGB image and convert to float32
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = image.astype(np.float32) / 255.0
# grayscale and blurring for canny edge detection
gray = cv2.cvtColor(orig_image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# carry out Canny edge detection
canny = cv2.Canny(blurred, 50, 200)
# initialize the structured edge detector with the model
edge_detector = cv2.ximgproc.createStructuredEdgeDetection('model.yml')
# detect the edges
edges = edge_detector.detectEdges(image)

plt.imshow(canny)
plt.show()
plt.imshow(edges)
plt.show()

norm_image = cv2.normalize(edges, None, alpha = 0, beta = 255, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_32F)
edges = norm_image.astype(np.uint8)
gry=edges
bw=cv2.threshold(gry, 5, 255, cv2.THRESH_BINARY)[1]

# Use floodfill to identify outer shape of objects
imFlood = bw.copy()
h, w = bw.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
cv2.floodFill(imFlood, mask, (0,0), 0)

cnts, hierarchy = cv2.findContours(imFlood, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
i=0
for cnt in cnts:
    # if the contour has no other contours inside of it
    if cv2.contourArea(cnt) > 500:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
        x, y, w, h = cv2.boundingRect(approx)
        bob = edges[y:y+h, x:x+w]
        cv2.rectangle(orig_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    i=i+1

plt.imshow(orig_image)
plt.show()
