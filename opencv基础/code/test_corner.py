import cv2
import numpy as np

image = cv2.imread('test.png')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
corners=cv2.goodFeaturesToTrack(gray,100,0.01,10) #(返回点个数，点质量，点距离)

for corner in corners:
     x,y= corner.ravel()  #降维
     cv2.circle(image,(int(x),int(y)),3,255,-1)  #画圆
cv2.imshow('Corners',image)
cv2.waitKey(0)
cv2.destroyAllWindows()