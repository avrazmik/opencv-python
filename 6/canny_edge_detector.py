import numpy as np
import cv2

chess = cv2.imread(
    "C:\\Users\\Y9ESEH724\\cv\\img\\Computer-Vision-with-Python\\DATA\\sammy_face.jpg"
)
blurred_image = cv2.blur(chess, (5, 5))
medianPixelVal = np.median(blurred_image)
lower = int(max(0, 0.7 * medianPixelVal))
higher = int(min(255, 1.3 * medianPixelVal))
result = cv2.Canny(chess, lower, higher)
cv2.imshow("edges", result)
cv2.waitKey(0)
