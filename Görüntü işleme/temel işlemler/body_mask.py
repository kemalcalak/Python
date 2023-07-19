import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def nothing(x):
    pass


cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 500, 500)

cv2.createTrackbar("L - H", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbar", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbar", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbar", 255, 255, nothing)

cv2.setTrackbarPos("U - H", "Trackbar", 180)
cv2.setTrackbarPos("U - S", "Trackbar", 255)
cv2.setTrackbarPos("U - V", "Trackbar", 255)

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L - H", "Trackbar")
    l_s = cv2.getTrackbarPos("L - S", "Trackbar")
    l_v = cv2.getTrackbarPos("L - V", "Trackbar")
    u_h = cv2.getTrackbarPos("U - H", "Trackbar")
    u_s = cv2.getTrackbarPos("U - S", "Trackbar")
    u_v = cv2.getTrackbarPos("U - V", "Trackbar")

    lower_color = np.array([l_h, l_s, l_v])
    upper_color = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_color, upper_color)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
