import cv2

# Read images
# img = cv2.imread('resources/dog.jpg')
# cv2.imshow('Output', img)
# # Wait images (miliseconds) / 0 == infinite
# cv2.waitKey(3000)

# Read Video
cap = cv2.VideoCapture('resources/We Are Abandoned Puppies.mp4')
while True:
    success, img = cap.read()  # return boolean and img
    cv2.imshow('Video', img)
    # break loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Read WebCam
# cap = cv2.VideoCapture(0)  # default webcam
# cap.set(3, 640)  # width=3, size=640
# cap.set(4, 480)  # height=4, size=480
# cap.set(10, 100)  # brightness=10

# while True:
#     success, img = cap.read()
#     cv2.imshow('WebCam', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
