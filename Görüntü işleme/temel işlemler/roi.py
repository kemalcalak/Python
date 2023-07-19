# roi --> region of interest --> ilgi alanı
import cv2
import numpy as np

img = cv2.imread("C:\Kodlar\python\Görüntü işleme\temel işlemler\klon.jpg")

roi = img[30:200, 200:400]

cv2.imshow("klon Asker", img)
cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
