import cv2
import numpy as np
from PIL import ImageGrab


def capture_image_and_different_image():

    different_count = 0
    threshold = 0.8
    picture_to_check = "controlpic.png"

    # screen capture
    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    # load picture to compare
    check_image = cv2.imread(picture_to_check)
    check_image = cv2.cvtColor(check_image, cv2.COLOR_BGR2GRAY)

    different = cv2.matchTemplate(frame, check_image, cv2.TM_CCOEFF_NORMED)

    location = np.where(different > threshold)

    for i in range(5):
        try:
            if location[0][i] in range(1000):
                different_count += 1

            else:
                pass

        except IndexError:
            pass

    return different_count