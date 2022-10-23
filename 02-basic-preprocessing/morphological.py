from turtle import back
import numpy as np
import cv2

background = (
    cv2.imread(
        "C:/Users/Y9ESEH724/cv/img/Computer-Vision-with-Python/DATA/dog_backpack.jpg",
    ).astype(np.float32)
    / 255
)

background = cv2.resize(background, dsize=(600, 600))

redchannel = background[:, :, 0].reshape((600, 600, 1))

data = np.random.random_integers(low=0, high=1, size=(600, 600, 1))
data = data.astype(np.float32).reshape(600, 600, 1)

# result = cv2.addWeighted(src1=redbackground, alpha=0.7, src2=data, beta=0.3, gamma=0.0)
# result = redbackground + data
redchannel[redchannel > 0.5] = 0.0
cv2.imshow("xyz", redchannel)
cv2.waitKey(0)
