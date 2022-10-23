from pickletools import uint8
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

"""
pic = Image.open("img/001 - factory.jpg")
arr = np.asarray(pic)
redChannel = arr[:, :, 0]
greenChannel = arr[:, :, 1]
blueChannel = arr[:, :, 2]
"""

import cv2


source = np.zeros(shape=(500, 500, 3), dtype=np.uint8)

for text in ["Hello", "Razmik", "How are you?"]:
    blank = source.copy()
    cv2.putText(blank, text, (20, 400), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255))
    cv2.imshow("blank", blank)
    if cv2.waitKey(1000) & 0xFF == 27:
        cv2.destroyAllWindows()
        exit(0)
exit(0)
source1 = cv2.imread("img/001 - factory.jpg")

"""
for r in range(255):
    for g in range(255):
        for b in range(255):
            blank = source1.copy()
            color = (b, g, r)
            cv2.rectangle(blank, (10, 400), (40, 450), color=color, thickness=-1)
            cv2.circle(blank, (200, 200), 50, color=color, thickness=-1)
            cv2.line(blank, (10, 10), (50, 50), color=color)
            cv2.imshow("blank", blank)
            print("processing {} {} {}".format(*color))
            if cv2.waitKey(1) & 0xFF == 27:
                cv2.destroyAllWindows()
                exit(0)
"""
exit(0)


img = cv2.imread("img/001 - factory.jpg")
# imgconverted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
while True:
    cv2.imshow("areal", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
