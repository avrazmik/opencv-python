import numpy as np
import cv2

DATA_PATH = "C:/Users/Y9ESEH724/cv/img/Computer-Vision-with-Python/DATA"
nadia = img = cv2.imread(DATA_PATH + "/Nadia_Murad.jpg", 0)

classifier = cv2.CascadeClassifier(
    DATA_PATH + "/haarcascades/haarcascade_frontalface_default.xml"
)

detected_faces = classifier.detectMultiScale(nadia)

for (x, y, w, h) in detected_faces:
    cv2.rectangle(nadia, (x, y), (x + w, y + h), (255, 255, 255))

cv2.imshow("Nadia", nadia)
cv2.waitKey(0)
