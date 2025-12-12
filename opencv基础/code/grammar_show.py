import cv2
import numpy as np   #opencv2中处理图像时常用到numpy
#############################
#.  image=cv2.imread('test.png')  #读取图像
#.  print(image.shape)          #打印图像的尺寸
#.  cv2.imshow('Image',image)
#.  cv2.waitKey(0)
############################
#.  crop=image[50:150,100:200]   #裁剪，注意格式为[行，列]
#.  cv2.imshow('Crop',crop)
#############################
image_1=np.zeros((300,300,3),np.uint8)  #创建一个300*300的黑色图像
cv2.line(image_1,(0,0),(300,300),(255,0,0),5)  #画一条蓝色线，起点，终点，颜色，线宽
cv2.rectangle(image_1,(50,50),(250,250),(0,255,0),3)  #画一个绿色矩形，左上角坐标，右下角坐标，颜色，线宽
cv2.circle(image_1,(150,150),100,(0,0,255),-1)  #画一个红色实心圆，圆心坐标，半径，颜色，填充
cv2.putText(image_1,'OpenCV',(70,150),0,1,(255,255,255),2)  #写字，内容，左下角坐标，字体，字号，颜色，线宽
cv2.imshow('Image_1',image_1)
cv2.waitKey(0)
#############################
