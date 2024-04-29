import cv2
import numpy as np

CAMERA_ID = 0
cam = cv2.VideoCapture(CAMERA_ID)

if not cam.isOpened():
    print('Cannot open the camera-%d' % (CAMERA_ID))
    exit()

cv2.namedWindow('CAM Window')

background = False
binary_mode = False

while True:
    ret, frame = cam.read()

    if not ret:
        break
    cv2.imshow('CAM Window', frame)
    key = cv2.waitKey(33)

    if key == ord('a'):
        # 배경 영상 촬영
        background= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        a = True

    elif key == ord('b'):
        # 이진화 모드 전환
        binary_mode = not binary_mode

    elif key == ord('q'):
        break

    if binary_mode and background is not None:
        # 차영상 계산
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(gray_frame, background)
        
        # 이진화
        _, binary_diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
        cv2.imshow("Binary Difference", binary_diff)

cam.release()
cv2.destroyAllWindows()
