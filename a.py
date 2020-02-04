import cv2 as cv
import numpy as np


image = cv.imread('conc_image.jpg')

cv.imshow('', image)

image = image[:250, 700:-700]

cv.imshow('a', image)

image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

image = cv.GaussianBlur(image,(7,7),0)

low = np.array((0, 0, 0), np.uint8)

high = np.array((120, 180, 255), np.uint8)
print(low, high)
cr = cv.inRange(image, low, high)

cv.imshow('filter', cr)
