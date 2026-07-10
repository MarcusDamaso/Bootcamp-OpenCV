import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

img_NZ_bgr = cv2.imread("New_Zealand_Boat.jpg",cv2.IMREAD_COLOR)
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr,cv2.COLOR_BGR2RGB)

img_NZ_rgb_flippedh = cv2.flip(img_NZ_rgb,1)
img_NZ_rgb_flippedv = cv2.flip(img_NZ_rgb,0)
img_NZ_rgb_flippedb = cv2.flip(img_NZ_rgb,-1)

plt.figure(figsize=[18,5])
plt.subplot(141);plt.imshow(img_NZ_rgb_flippedh);plt.title("Imagem girada horizontalmente")
plt.subplot(142);plt.imshow(img_NZ_rgb_flippedv);plt.title("Imagem girada verticalmente")
plt.subplot(143);plt.imshow(img_NZ_rgb_flippedb);plt.title("Imagem girada nas 2 direções")
plt.subplot(144);plt.imshow(img_NZ_rgb);plt.title("OG")
plt.show()