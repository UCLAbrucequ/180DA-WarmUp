import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import helpers


cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    # mask of blue
    mask1 = cv.inRange (hsv, lower_blue, upper_blue)

    res = cv.bitwise_and(frame, frame, mask=mask1)

    ret, thresh = cv.threshold(mask1.copy(), 127, 255, 0)
    contours, _ = cv.findContours(thresh, 1, 2)
    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)
        if cv.contourArea(contour) < 1000:
            continue
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        cv.putText(frame, "Status: {}".format('Movement'), (10, 20), cv.FONT_HERSHEY_SIMPLEX, \
                    1, (0, 0, 255), 3)

    cv.imshow('frame',frame)

    k = cv.waitKey(5) 
    if k == 27:
        break

cv.destroyAllWindows()
cap.release()


######################################
## Testing functions in helper.py
######################################

# img = cv.imread("/Users/brucequ/Documents/180DA-WarmUp/Images/test_image2.jpeg", -1)
# imgray = cv.imread("/Users/brucequ/Documents/180DA-WarmUp/Images/test_image2.jpeg", 0)
# result = helpers.adaptive_threshold(imgray)
# result = helpers.Otsu_Gaussian(imgray)
# ret, thresh = cv.threshold(imgray, 127, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# cv.drawContours(img, contours, -1, (0,255,0), 3)

# # Display OTSU threshold
# while(1):
#     cv.imshow("Adaptive_threshold", result)
#     k = cv.waitKey(5) & 0xFF
#     if k == 27:
#         break
# cv.destroyAllWindows()

# # Canny Edge Detection
# edges = cv.Canny(imgray, 100, 200)
# plt.subplot(121), plt.imshow(imgray, cmap='gray')
# plt.title("Original Image"), plt.xticks([]), plt.yticks([])

# plt.subplot(122), plt.imshow(edges, cmap='gray')
# plt.title("Edge Image"), plt.xticks([]), plt.yticks([])

# plt.show()

# Bounding Rectangles
# helpers.bounding_rect(imgray)
