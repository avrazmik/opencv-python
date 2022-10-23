import numpy as np
import cv2

background = cv2.imread(
    "C:/Users/Y9ESEH724/cv/img/Computer-Vision-with-Python/DATA/dog_backpack.jpg"
)
watermark = cv2.imread(
    "C:/Users/Y9ESEH724/cv/img/Computer-Vision-with-Python/DATA/watermark_no_copy.png"
)

watermark = cv2.resize(watermark, (400, 400))

offsetX = 0
offsetY = 0

background[0:400, 0:400] = watermark
cv2.imshow("Overlay", background)
cv2.waitKey(0)
exit(0)
