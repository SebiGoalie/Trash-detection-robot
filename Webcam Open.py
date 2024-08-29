import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0, apiPreference=cv.CAP_AVFOUNDATION)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    ret, frame = cap.read()
    
    
    if not ret:
        print("Can't receive frame")
        break
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    cv.imshow('color',frame)
   
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()