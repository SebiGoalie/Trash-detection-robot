import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    #blur function, uses square 
    blurred = cv.GaussianBlur(frame, (9,9),0)
    cv.imshow('Gaussian', blurred)
    if not ret:
        print("Can't receive frame")
        break
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    cv.imshow('color',frame)
   
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()
