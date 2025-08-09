# 1. Importing Dependencies
import cv2
import numpy as np

# 2. Loading the input image
image = cv2.imread("input.png")
cv2.imshow('nis', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

