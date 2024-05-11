import cv2
import numpy as np

def apply_filter(frame, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
    filtered_frame = cv2.filter2D(frame, -1, kernel)
    return filtered_frame

def on_trackbar_change(val):
    global filter_size, frame
    filter_size = val
    filtered_frame = apply_filter(frame, filter_size)
    cv2.imshow('Filtered Frame', filtered_frame)

CAMERA_ID = 0
cam = cv2.VideoCapture(CAMERA_ID)
if not cam.isOpened():
    print('Cannot open the camera-%d' % (CAMERA_ID))
    exit()

cv2.namedWindow('CAM Window')

filter_size = 1  
ret, frame = cam.read()  


cv2.createTrackbar('Filter Size', 'CAM Window', filter_size, 20, on_trackbar_change)

while True:
    cv2.imshow('CAM Window',frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    ret,frame = cam.read() 

cam.release()
cv2.destroyAllWindows()
