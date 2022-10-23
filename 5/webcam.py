import numpy as np
import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

writer = cv2.VideoWriter(
    "mysuper.mp4v", cv2.VideoWriter_fourcc(*"DIVX"), 30, (width, height)
)

while True:
    ret, frame = cap.read()
    # cv2.cvtColor(frame, cv2.color+BGR)
    writer.write(frame)
    cv2.imshow("Image", frame)
    # print("{} {} {}".format(width, height, count))
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
