import numpy as np
import cv2

capture = cv2.VideoCapture(0)
ret, frame = capture.read(0)

roi = cv2.selectROI("roi selection", frame)

cv2.destroyWindow("roi selection")
# tracker = cv2.TrackerMIL_create()
tracker = cv2.legacy.TrackerBoosting_create()
tracker.init(frame, roi)

while True:

    ret, next = capture.read(0)
    success, roi = tracker.update(next)

    if success:
        (x, y, w, h) = np.int0(roi)

        cv2.rectangle(next, (x, y), (x + w, y + h), (0, 255, 0))

    cv2.imshow("current", next)
    if cv2.waitKey(30) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()
