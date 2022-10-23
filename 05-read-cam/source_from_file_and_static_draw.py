import re
import numpy as np
import cv2
import time

cap = cv2.VideoCapture(
    "C:\\Users\\Y9ESEH724\\cv\\img\\Computer-Vision-with-Python\\DATA\\finger_move.mp4"
)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        time.sleep(1 / 20) # 20 fps
        frame = cv2.rectangle(
            frame, (0, 0), (int(width / 2), int(height / 2)), (0, 0, 255), -1
        )
        cv2.imshow("img", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
