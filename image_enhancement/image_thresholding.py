import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image

img_read = cv2.imread("building-windows.jpg", cv2.IMREAD_GRAYSCALE)
retval, img_thresh = cv2.threshold(img_read, 100, 255, cv2.THRESH_BINARY)#se o pixel for maior que 100 ele vira branco 255 caso nao vira 0 preto

plt.figure(figsize=[18,5])
plt.subplot(121); plt.imshow(img_read, cmap="gray");plt.title("Original")
plt.subplot(122); plt.imshow(img_thresh, cmap="gray"); plt.title("Thresholded")
plt.show()

print(img_thresh.shape)