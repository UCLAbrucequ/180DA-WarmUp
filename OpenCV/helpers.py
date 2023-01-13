import cv2 as cv
from matplotlib import pyplot as plt

def display(path, flag):
    """
    Displays the image following the path
    INPUT:
    - flag:
        -1: IMREAD_UNCHANGED
        0: IMREAD_GRAYSCALE
        1: IMREAD_COLOR
    """
    while(1):
        img = cv.imread(path, flag)
        cv.imshow("Image", img)
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()
