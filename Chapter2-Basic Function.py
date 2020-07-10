import cv2
import numpy as np

img = cv2.imread('resources/dog.jpg')
kernel = np.ones((5, 5), np.uint8)

# Convert to Grey Scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", imgGray)
# cv2.waitKey(5000)

# Convert to Blur
imgBlur = cv2.GaussianBlur(imgGray, (33, 33), 0)  # kernel size
# cv2.imshow('Blur', imgBlur)
# cv2.waitKey(5000)

# Edge detector
imgCanny = cv2.Canny(img, 70, 70)  # threshold =
# cv2.imshow('Edge Detector', imgCanny)
# cv2.waitKey(5000)

# Dialation = Increase thickness of edge
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)  # kernel
# cv2.imshow('Dialation', imgDialation)
# cv2.waitKey(5000)

# Eroded = decrease thickness of edge
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
# cv2.imshow("Eroded Image", imgEroded)
# cv2.waitKey(5000)

# Find size of images
# print(img.shape)  # height, width, chanel
imgResize = cv2.resize(img, (300, 200))  # width, height
# cv2.imshow("Resized", imgResize)
# cv2.waitKey(3000)

# Crop Image
imgCropped = img[0:200, 200:500]  # start and end point (height, width)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(3000)
