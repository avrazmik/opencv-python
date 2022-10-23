import numpy as np
import cv2


def drawLine(img, p1, p2, color):
    startX, startY = p1
    endX, endY = p2
    steps = max(endY - startY, endX - startX)
    xInc = (endX - startX) / steps
    yInc = (endY - startY) / steps
    while startX <= endX and startY <= endY:
        img[int(startX)][int(startY)] = np.asarray(color)
        print("{} {}".format(startY, startY))
        startX = startX + xInc
        startY = startY + yInc


img = np.zeros(shape=(600, 600, 3), dtype=np.uint8)
drawLine(img, (0, 0), (200, 100), (0, 0, 255))
cv2.imshow("img", img)
cv2.waitKey(0)
