import numpy as np
import cv2

img1 = cv2.imread(
    "C:/Users/Y9ESEH724/cv/img/Computer-Vision-with-Python/DATA/watermark_no_copy.png"
)
img2 = cv2.imread(
    "C:/Users/Y9ESEH724/cv/img/Computer-Vision-with-Python/DATA/dog_backpack.jpg"
)

img1 = cv2.resize(img1, (1200, 1200))
img2 = cv2.resize(img2, (1200, 1200))

img3 = cv2.addWeighted(img2, 0.5, img1, 0.5, 0)
cv2.imshow("Blended", img3)
cv2.waitKey(0)
exit(0)
