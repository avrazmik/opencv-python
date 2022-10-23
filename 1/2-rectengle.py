import numpy as np
import cv2

WIN_NAME = "Drawing 002-2"


backup = np.zeros(shape=(500, 500, 3), dtype=np.uint8)
img = backup.copy()

color = (0, 255, 0)
firstPointClicked = None


def mouseCallback(event: int, x: int, y: int, flags: int, params):
    global color, firstPointClicked, backup, img
    if event == cv2.EVENT_LBUTTONDOWN:
        firstPointClicked = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if firstPointClicked is not None:
            img = backup.copy()
            cv2.rectangle(img, firstPointClicked, (x, y), color)
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(backup, firstPointClicked, (x, y), color)
        img = backup.copy()
        firstPointClicked = None


cv2.namedWindow(WIN_NAME)
cv2.setMouseCallback(WIN_NAME, mouseCallback)

while True:
    cv2.imshow(WIN_NAME, img)
    if cv2.waitKey(10) & 0xFF == 27:
        cv2.destroyAllWindows()
        exit(0)
