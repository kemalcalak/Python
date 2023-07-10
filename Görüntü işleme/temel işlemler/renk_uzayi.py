import cv2

img = cv2.imread("klon.jpg")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

cv2.imshow("img", img)
cv2.imshow("img_rgb", img_rgb)
cv2.imshow("img_hsv", img_hsv)
cv2.imshow("img_gray", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
