import numpy as np
import cv2


def resize(frame):
    scale_percent = 50  # percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


capture = cv2.VideoCapture(0)
ret, prev_frame = capture.read(0)
# prev_frame = resize(prev_frame)
prvs = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

hsv = np.zeros_like(prev_frame)
hsv[..., 1] = 255

while True:
    ret, frame = capture.read(0)
    if not ret:
        print("No frames grabbed!")
        break
    # frame = resize(frame)
    next = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow("bg", bgr)
    cv2.imshow("current", frame)
    if cv2.waitKey(30) & 0xFF == 27:
        break

    prvs = next


capture.release()
cv2.destroyAllWindows()
