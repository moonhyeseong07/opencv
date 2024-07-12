import numpy as np
import cv2
from matplotlib import pyplot as plt

img1_src = cv2.imread("img6.jpg",cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1_src, (320,240))

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(img1, 1.1, 3)
res1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)

for (x,y,w,h) in faces:
    cv2.rectangle(res1, (x,y), (x+w, y+h), (255, 0, 0), 2)
    
displays = [("input1",img1),
            ("res1", res1)]

for (name,out) in displays:
    cv2.imshow(name, out)

cv2.waitKey(0)
cv2.destroyAllWindows()