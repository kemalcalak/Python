import cv2
import numpy as np

img = cv2.imread("C:\Kodlar\python\Görüntü işleme\temel işlemler\klon.jpg")
dimesnion = img.shape
print(dimesnion)

color = img[420, 500]
print(color)
print("BGR: ", color)

blue = img[420, 500, 0]
print("Blue: ", blue)

green = img[420, 500, 1]
print("Green: ", green)

red = img[420, 500, 2]
print("Red: ", red)

img[420, 500] = 250
print("new blue: ", img[420, 500])

blue1 = img.item(150, 200, 0)
print("Blue1: ", blue1)
img.itemset((150, 200, 0), 172)
print("new blue1: ", img(150, 200, 0))

cv2.imshow("klon Asker", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
