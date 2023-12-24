import cv2
import numpy as np

img = cv2.imread("helikopter.jpg",0)
row,col = img.shape

M= np.float32([[1,0,50],[0,1,200]])

dst = cv2.warpAffine(img,M,(row,col))

cv2.imshow("dst",dst)
