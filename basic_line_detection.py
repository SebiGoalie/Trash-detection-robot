import cv2 as cv
import numpy as np
import matplotlib
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt

kernel_size = 3 #setup kernel size for detection
def nothing(x):#create function that passes nothing
    pass
rho = 1# distance res of pixels in grid
theta = np.pi/180
threshold = 15
min_line_length = 50
max_line_gap = 20


cap = cv.VideoCapture(0) #start video capture
cv.namedWindow("edge_thresholding",cv.WINDOW_NORMAL)
cv.createTrackbar('low_thresholdT','edge_thresholding',0,300, nothing)
cv.createTrackbar('high_thresholdT', 'edge_thresholding',0,500,nothing)


if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    low_threshold = cv.getTrackbarPos('low_thresholdT','edge_thresholding')
    high_threshold = cv.getTrackbarPos('high_thresholdT','edge_thresholding')
    ret, frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    blur_gray = cv.GaussianBlur(gray,(kernel_size, kernel_size),0)
    edges = cv.Canny(blur_gray, low_threshold, high_threshold)
    line_image = np.copy(frame)*0
    lines = cv.HoughLinesP(edges,rho,theta,threshold,np.array([]),min_line_length, max_line_gap)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)
    lines_edges = cv.addWeighted(frame,0.8,line_image,1,0)
    if not ret:
        print("Can't receive frame")
        break
    
    
    cv.imshow('color',line_image)
   
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()
