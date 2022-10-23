from turtle import back
import numpy as np
import cv2

background = cv2.imread(
    "C:/Users/Y9ESEH724/cv/img/Computer-Vision-with-Python/DATA/dog_backpack.jpg",
    cv2.IMREAD_GRAYSCALE,
)


def custom():

    WIN_NAME = "Drawing 002-2"

    redThreshhold = 0

    def mouseCallback(event: int, x: int, y: int, flags: int, params):
        global redThreshhold
        if event == cv2.EVENT_MOUSEWHEEL:
            redThreshhold = redThreshhold + 5
            if redThreshhold >= 255:
                redThreshhold = 0

    cv2.namedWindow(WIN_NAME)
    cv2.setMouseCallback(WIN_NAME, mouseCallback)

    background = cv2.resize(background, (400, 400))

    while True:
        newImg = np.zeros((background.shape[0], background.shape[1], 1), dtype=np.uint8)
        rows, cols, channels = newImg.shape
        for row in range(rows):
            for col in range(cols):
                newImg[row, col] = 255 if background[row, col, 0] > redThreshhold else 0

        cv2.imshow(WIN_NAME, newImg)

        if cv2.waitKey(10) & 0xFF == 27:
            cv2.destroyAllWindows()
            exit(0)


threshhold, result = cv2.threshold(background, 122, 255, type=cv2.THRESH_BINARY)
cv2.imshow("result", result)
cv2.waitKey(0)
