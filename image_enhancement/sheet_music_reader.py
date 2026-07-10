import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image

img_read = cv2.imread("Piano_Sheet_Music.png", cv2.IMREAD_GRAYSCALE)

retval, img_thresh_gb_1 = cv2.threshold(img_read, 50, 255, cv2.THRESH_BINARY)
retval, img_thresh_gb_2 = cv2.threshold(img_read,130,255, cv2.THRESH_BINARY)

img_thresh_adp = cv2.adaptiveThreshold(img_read,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

plt.figure(figsize=[18,15])
plt.subplot(221);plt.imshow(img_read, cmap='gray');plt.title('original')
plt.subplot(222); plt.imshow(img_thresh_gb_1,cmap='gray'); plt.title('Thresholded (global: 50)');
plt.subplot(223); plt.imshow(img_thresh_gb_2,cmap='gray'); plt.title('Thresholded (global: 130)');
plt.subplot(224); plt.imshow(img_thresh_adp,cmap='gray'); plt.title('Thresholded (adaptative)');


plt.show()