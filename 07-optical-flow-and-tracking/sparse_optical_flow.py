import numpy as np
import cv2
import time

capture = cv2.VideoCapture(0)
ret, prev_frame = capture.read(0)
gray_prev = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)


prev_corners = cv2.goodFeaturesToTrack(
    gray_prev, maxCorners=10, qualityLevel=0.01, minDistance=10
)

lk_params = dict(
    winSize=(15, 15),
    maxLevel=2,
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03),
)

while True:
    """
    corners = np.int0(corners)
    for corner in corners:
        corner = corner[0]
        cv2.circle(frame, (corner[0], corner[1]), 5, (255, 0, 0))
    """

    ret, frame = capture.read(0)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    p1, st, err = cv2.calcOpticalFlowPyrLK(
        gray_prev, gray_frame, prev_corners, None, **lk_params
    )

    if p1 is not None:
        good_new = p1[st == 1]
        good_old = prev_corners[st == 1]

        for i in range(len(good_new)):
            cv2.line(
                frame,
                (int(good_new[i][0]), int(good_new[i][1])),
                (int(good_old[i][0]), int(good_old[i][1])),
                color=(0, 255, 0),
                thickness=3,
            )
            """
            cv2.circle(
                frame,
                (int(good_new[i][0]), int(good_new[i][1])),
                8,
                color=(0, 255, 0),
            )
            """
    else:
        print("Resetting points...")
        prev_corners = cv2.goodFeaturesToTrack(
            gray_prev, maxCorners=10, qualityLevel=0.01, minDistance=10
        )
        continue

    cv2.imshow("current", frame)
    if cv2.waitKey(30) & 0xFF == 27:
        break

    gray_prev = gray_frame.copy()
    prev_corners = good_new.reshape(-1, 1, 2)

capture.release()
cv2.destroyAllWindows()
