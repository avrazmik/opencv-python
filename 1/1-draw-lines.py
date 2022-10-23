import numpy as np
import cv2

WIN_NAME = "Drawing"


backup = np.zeros(shape=(500, 500, 3), dtype=np.uint8)
img = backup.copy()

color = (255, 0, 0)
priorPointClicked = None


def mouseCallback(event: int, x: int, y: int, flags: int, params):
    global color, priorPointClicked, backup, img

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 2, color=color)
        if priorPointClicked is not None:
            cv2.line(img, priorPointClicked, (x, y), color)
        priorPointClicked = (x, y)
    elif event == cv2.EVENT_RBUTTONDOWN:
        tmp = (color[1], color[2], color[0])
        color = tmp
        print("new color {}", color)
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("reset canvas")
        img = backup.copy()
        priorPointClicked = None


cv2.namedWindow(WIN_NAME)
cv2.setMouseCallback(WIN_NAME, mouseCallback)

while True:
    cv2.imshow(WIN_NAME, img)
    if cv2.waitKey(10) & 0xFF == 27:
        cv2.destroyAllWindows()
        exit(0)
