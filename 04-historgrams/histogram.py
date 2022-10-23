import enum
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(
    "C:\\Users\\Y9ESEH724\\cv\\img\\Computer-Vision-with-Python\\DATA\\bricks.jpg"
)

for i, c in enumerate(("b", "g", "r")):
    hist = cv2.calcHist([img], [i], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color=c)
plt.show()
# cv2.imshow("img", img)
# cv2.waitKey(0)
print("done")
