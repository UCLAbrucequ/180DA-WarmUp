import cv2 as cv

def display(path):
    while(1):
        img = cv.imread(path, 0)
        cv.imshow("Image", img)
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()

