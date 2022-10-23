from operator import inv
from turtle import back
import numpy as np
import cv2

background = cv2.imread(
    "C:/Users/Y9ESEH724/cv/img/Computer-Vision-with-Python/DATA/dog_backpack.jpg"
)
watermark = cv2.imread(
    "C:/Users/Y9ESEH724/cv/img/Computer-Vision-with-Python/DATA/watermark_no_copy.png"
)
watermark = cv2.resize(watermark, (400, 400))

grayWatermark = cv2.cvtColor(watermark, cv2.COLOR_RGB2GRAY)
inverseWatermark = cv2.bitwise_not(grayWatermark)

whiteBg = np.full(watermark.shape, 255, dtype=np.uint8)

watermarkToApply = cv2.bitwise_or(whiteBg, whiteBg, mask=inverseWatermark)

wrows, wcols, wchannels = watermarkToApply.shape
brows, bcols, bchannels = background.shape


roi = background[brows - wrows - 1 : brows - 1, bcols - wcols - 1 : bcols - 1]
roi = cv2.bitwise_or(roi, watermarkToApply)

background[brows - wrows - 1 : brows - 1, bcols - wcols - 1 : bcols - 1] = roi

cv2.imshow("background", background)
cv2.waitKey(0)
