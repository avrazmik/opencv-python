import numpy as np
import cv2
import matplotlib.pyplot as plt

full = cv2.imread(
    "C:\\Users\\Y9ESEH724\\cv\\img\\Computer-Vision-with-Python\\DATA\\sammy_noise.jpg"
)

face = cv2.imread(
    "C:\\Users\\Y9ESEH724\\cv\\img\\Computer-Vision-with-Python\\DATA\\sammy_face.jpg"
)

res = cv2.matchTemplate(full, face, cv2.TM_CCOEFF)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

height, width, channels = face.shape
top_left = max_loc
# buttom_right = (top_left[0] + width, top_left[1] + height)
# full = cv2.circle(full, min_loc, 5, color=(0, 0, 255))
# full = cv2.circle(full, max_loc, 5, color=(0, 0, 255))
full = cv2.rectangle(
    full, top_left, (top_left[0] + width, top_left[1] + height), color=(0, 0, 255)
)

result = cv2.addWeighted(full[:, :, 0], 0.5, res, 0.5, 0)
# plt.imshow(res)
plt.imshow(result)
plt.show()
# cv2.imshow("full", full)
# cv2.imshow("hist", full)
# cv2.waitKey(0)
