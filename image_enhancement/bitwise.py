import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image

img_rec = cv2.imread("rectangle.jpg", cv2.IMREAD_GRAYSCALE)
img_circ = cv2.imread("circle.jpg",cv2.IMREAD_GRAYSCALE)

"""plt.figure(figsize=[20,5])
plt.subplot(121);plt.imshow(img_rec,cmap='gray')
plt.subplot(122);plt.imshow(img_circ,cmap='gray')"""

#operação and bitwise
result = cv2.bitwise_and(img_rec, img_circ, mask=None)
plt.imshow(result,cmap='gray')

#operador bitwise ou

result = cv2.bitwise_or(img_rec, img_circ, mask= None)
plt.imshow(result,cmap='gray')

#operador bitwise "ou exclusivo"

result = cv2.bitwise_xor(img_rec, img_circ, mask = None)
plt.imshow(result, cmap='gray')
plt.show()