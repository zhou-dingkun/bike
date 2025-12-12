import cv2
import numpy as np

capture = cv2.VideoCapture(0) #摄像头编号

while True:
    ret, frame = capture.read()
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1)
    if key!= -1:
        break

capture.release()
cv2.destroyAllWindows()
