import cv2 as cv
from matplotlib import pyplot as plt

def display(flag, path=None):
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


def adaptive_threshold(imgray):
    result = cv.adaptiveThreshold(imgray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                    cv.THRESH_BINARY, 11, 2)
    return result

def Otsu_Gaussian(imgray):
    """
    Otsu's thresholding after Gaussian filtering

    """
    blur = cv.GaussianBlur(imgray, (5,5), 0)
    ret, result = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    return result
