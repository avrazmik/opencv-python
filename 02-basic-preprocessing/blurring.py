import cv2
import numpy as np


image = cv2.imread(
    "C:/Users/Y9ESEH724/cv/img/Computer-Vision-with-Python/DATA/bricks.jpg"
)


def gamma():
    image = image.astype(dtype=np.float32) / 255
    gamma = 5.0
    gammaImage = np.power(image, gamma)
    cv2.imshow("Bricks", gammaImage)
    cv2.waitKey(0)


def blur():
    blurredImage = cv2.blur(image, ksize=(9, 9))
    cv2.imshow("Bricks", blurredImage)
    cv2.waitKey(0)


blur()
