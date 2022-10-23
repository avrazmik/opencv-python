import numpy as np
import cv2

chess = cv2.imread(
    "C:\\Users\\Y9ESEH724\\cv\\img\\Computer-Vision-with-Python\\DATA\\flat_chessboard.png"
)

chess_grey = cv2.cvtColor(chess, cv2.COLOR_BGR2GRAY).astype(np.float32)

corners = cv2.cornerHarris(chess_grey, 2, 3, 0.04)
corners = cv2.dilate(corners, None)
chess[corners > 0.01 * corners.max()] = (255, 0, 0)
cv2.imshow("chess", chess)
cv2.waitKey(0)
