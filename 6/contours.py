import numpy as np
import cv2

image = cv2.imread(
    "C:\\Users\\Y9ESEH724\\cv\\img\\Computer-Vision-with-Python\\DATA\\internal_external.png",
    0,
)
contours, hier = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

external_contours = np.zeros(image.shape)
for i in range(len(contours)):
    if hier[0][i][-1] != -1:
        cv2.drawContours(external_contours, contours, i, (255, 0, 0), -1)


cv2.imshow("contours", external_contours)
cv2.waitKey(0)
