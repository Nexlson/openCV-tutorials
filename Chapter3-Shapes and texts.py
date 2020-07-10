import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# img[:] = 255, 0, 0  # color whole img blue

# Draw Shapes
cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.rectangle(img, (300, 300), (325, 325), (255, 0, 0),
              cv2.FILLED)  # Filled rectangle
cv2.circle(img, (400, 50), (30), (255, 255, 0), 5)

# Add text
cv2.putText(img, "OpenCV", (300, 200),
            cv2.FONT_HERSHEY_COMPLEX, 1, (150, 400, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(3000)
