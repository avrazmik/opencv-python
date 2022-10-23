import numpy as np
import cv2

DATA_PATH = "C:/Users/Y9ESEH724/cv/img/Computer-Vision-with-Python/DATA"

traffic = cv2.imread(DATA_PATH + "/car_plate.jpg")
gray = cv2.cvtColor(traffic, cv2.COLOR_BGR2GRAY)

classifier = cv2.CascadeClassifier(
    DATA_PATH + "/haarcascades/haarcascade_russian_plate_number.xml"
)

detected_plates = classifier.detectMultiScale(gray, minNeighbors=5)
for (x, y, w, h) in detected_plates:
    # cv2.rectangle(traffic, (x, y), (x + w, y + h), color=(0, 0, 255))
    plate = traffic[y : y + h, x : x + w]
    plate = cv2.medianBlur(plate, 7)
    traffic[y : y + h, x : x + w] = plate

cv2.imshow("traffic", traffic)
cv2.waitKey(0)
