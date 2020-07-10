import cv2
import numpy as np

img = cv2.imread('resources/dog.jpg')

# Works if both have same num of channel
# Horizontal join
hor = np.hstack((img, img))
# Vertical Join
ver = np.vstack((img, img))

cv2.imshow('img', ver)
cv2.waitKey(2000)
