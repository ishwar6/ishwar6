import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
blank[:] = 0, 121, 1
print(blank)

cv.imshow('Blank', blank)

cv.waitKey(0)
