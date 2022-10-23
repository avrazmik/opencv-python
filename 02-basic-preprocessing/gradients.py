import cv2
import numpy as np


img = cv2.imread(
    "C:\\Users\\Y9ESEH724\\cv\\img\\Computer-Vision-with-Python\\DATA\\sudoku.jpg", 0
)
resx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
resy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
cv2.imshow("resx", resx)
cv2.imshow("resy", resy)
cv2.waitKey(0)
