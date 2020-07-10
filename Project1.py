import cv2

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 130)


def findColor(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([])


while True:
    success, img = cap.read()
    cv2.imread("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
