import cv2

###################################
# 图像平滑处理-去噪声
###################################
cv2.imread('test.png')

guass=cv2.GaussianBlur(cv2.imread('test.png'),(5,5),0)
median=cv2.medianBlur(cv2.imread('test.png'),5) #中值滤波

cv2.imshow('Original',cv2.imread('test.png'))
cv2.imshow('Guassian Blur',guass)
cv2.imshow('Median Blur',median)
cv2.waitKey(0)