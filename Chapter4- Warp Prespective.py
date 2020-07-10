import cv2
import numpy as np
img = cv2.imread('resources/cards.jpeg')
width, height = 250, 350
# Origin position
pts1 = np.float32([[45, 23], [96, 19], [44, 101], [97, 100]])
# New position
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('img', imgOutput)
cv2.waitKey(3000)
