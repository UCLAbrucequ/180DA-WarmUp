import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

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


def bounding_rect(imgray):
    """
    display the center of the mass
    """
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, 1, 2)
    cnt = contours[0]
    x,y,w,h = cv.boundingRect(cnt)
    cv.rectangle(imgray, (x,y), (x+w, y+h), (0, 255, 0), 2)
    rect = cv.minAreaRect(cnt)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    cv.drawContours(imgray, [box], -1, (0,255,0), 3)
    cv.imshow("Grayscale Image", imgray)


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist


def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar


def find_dominant_color(frame):
    # Convert BGR to RGB
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    rgb = rgb.reshape((rgb.shape[0] * rgb.shape[1],3))
    clt = KMeans(n_clusters=3) #cluster number
    clt.fit(rgb)

    hist = find_histogram(clt)
    bar = plot_colors2(hist, clt.cluster_centers_)

    plt.axis("off")
    plt.imshow(bar)
    plt.show()
