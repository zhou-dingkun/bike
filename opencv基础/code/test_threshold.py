import cv2
import numpy as np

gray=cv2.imread("car.png",cv2.IMREAD_GRAYSCALE)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#二分法
thresh_adp=cv2.adaptiveThreshold(gray,255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#内置自适应分配算法
thresh_otsu=cv2.threshold(gray,0,255,
    cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
#大津法

cv2.imshow("Gray",gray)
cv2.imshow("Threshold Adaptive",thresh_adp)
cv2.imshow("Threshold Otsu",thresh_otsu)
cv2.imshow("Threshold Binary",thresh)
cv2.waitKey(0)