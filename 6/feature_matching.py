import numpy as np
import cv2


def SIFT():
    single = cv2.imread(
        "C:\\Users\\Y9ESEH724\\cv\\img\\Computer-Vision-with-Python\\DATA\\reeses_puffs.png",
        0,
    )
    many = cv2.imread(
        "C:\\Users\\Y9ESEH724\\cv\\img\\Computer-Vision-with-Python\\DATA\\many_cereals.jpg",
        0,
    )

    sift = cv2.SIFT_create()
    kp1, ds1 = sift.detectAndCompute(single, None)
    kp2, ds2 = sift.detectAndCompute(many, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(ds1, ds2, k=2)

    good = []
    """
    for m1, m2 in matches:
        if 2.0 * m1.distance < m2.distance:
            print("good match {} {} ".format(m1.distance, m2.distance))
            good.append([m1])
    """

    matches = sorted(matches, key=lambda x: x[0].distance)[:25]

    fn = cv2.drawMatchesKnn(single, kp1, many, kp2, matches, None, flags=2)
    cv2.imshow("matches", fn)
    cv2.waitKey(0)


SIFT()
