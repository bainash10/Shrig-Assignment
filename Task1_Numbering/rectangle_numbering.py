# 1. Importing Dependencies
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 2. Loading the input image
image = cv2.imread("input.png")

# Backing up the original image to drawing results later on
orig_image = image.copy()

# 3. Preprocessing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur=cv2.GaussianBlur(gray,(5,5),0)

edges = cv2.Canny(blur, threshold1=50, threshold2=200)
