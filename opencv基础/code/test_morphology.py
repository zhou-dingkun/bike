import cv2
import numpy as np

gray=cv2.imread("opencv.png",cv2.IMREAD_GRAYSCALE)
_,binary=cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV) #二值化+反转
kernel=np.ones((5,5),np.uint8) #5x5 kernel of ones

dilication=cv2.dilate(binary,kernel,iterations=1)
erosion=cv2.erode(binary,kernel,iterations=1)
#清理图案细节
cv2.imshow("Original",binary)
cv2.imshow("Dilation",dilication)
cv2.imshow("Erosion",erosion)
cv2.waitKey(0)


