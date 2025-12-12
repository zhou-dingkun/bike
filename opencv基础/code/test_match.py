import cv2
import numpy as np

image=cv2.imread("poker.png")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

template=gray[130:230,350:450] #模板图像

match=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
locations=np.where(match>=0.9) #匹配阈值

w,h=template.shape[::-1]
for pt in zip(*locations[::-1]):
    cv2.rectangle(image,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)#画矩形框标记匹配位置
# 显示结果
cv2.imshow("Template",template)     
cv2.imshow("Match Result",image)
cv2.waitKey(0)