from msilib import change_sequence
import numpy as np
import cv2


chess = cv2.imread(
    "C:\\Users\\Y9ESEH724\\cv\\img\\Computer-Vision-with-Python\\DATA\\flat_chessboard.png"
)

chess_grey = cv2.cvtColor(chess, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(chess_grey, 10, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    chess = cv2.circle(chess, (x, y), 5, (255, 0, 0))

cv2.imshow("chess", chess)
cv2.waitKey(0)
