import cv2
import numpy as np
import time

camera = cv2.VideoCapture(0)
# camera = cv2.VideoCapture(1)

while True:
    # time.sleep(1)
    ret, frame = camera.read()
    # time.sleep(1)
    cv2.imshow('camera',frame)

    if cv2.waitLey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllwindows()