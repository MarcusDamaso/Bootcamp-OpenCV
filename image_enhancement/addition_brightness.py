import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image

img_bgr = cv2.imread("New_Zealand_Coast.jpg",cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)


matrix = np.ones(img_rgb.shape, dtype= "uint8") * 50

img_rgb_brighter = cv2.add(img_rgb, matrix)
img_rgb_darker = cv2.subtract(img_rgb, matrix)

plt.figure(figsize=[18,5])
plt.subplot(131);plt.imshow(img_rgb_darker);plt.title("Imagem mais escura")
plt.subplot(133);plt.imshow(img_rgb_brighter);plt.title("Imagem mais clara")
plt.subplot(132);plt.imshow(img_rgb);plt.title("OG")
plt.show()
