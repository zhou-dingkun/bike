import cv2

gray=cv2.imread("poker.png",cv2.IMREAD_GRAYSCALE)

laplacian=cv2.Laplacian(gray,cv2.CV_64F)
canny=cv2.Canny(gray,50,125)

 
cv2.imshow("Gray",gray)
cv2.imshow("Canny",canny)
cv2.waitKey(0)