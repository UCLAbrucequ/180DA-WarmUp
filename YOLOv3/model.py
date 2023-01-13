import cv2 as cv
import torch
from torch import hub
from matplotlib import pyplot as plt


model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)


imgs = [plt.imread("/Users/brucequ/Documents/180DA-WarmUp/Images/test_image4.jpeg", -1)]
results = model(imgs)
results.show()