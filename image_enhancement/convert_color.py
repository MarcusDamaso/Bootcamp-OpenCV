import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys



img_NZ = cv2.imread("New_Zealand_Lake.jpg")
img_NZ_rgb = cv2.cvtColor(img_NZ, cv2.COLOR_BGR2RGB)
img_NZ_hsv = cv2.cvtColor(img_NZ, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(img_NZ_hsv)

plt.figure(figsize=[24,10])

plt.subplot(231);plt.imshow(img_NZ);plt.title("Imagem BGR Original")
plt.subplot(232);plt.imshow(img_NZ_rgb);plt.title("Imagem RGB convertida")
plt.subplot(233);plt.imshow(h,cmap='gray');plt.title("Canal H")
plt.subplot(234);plt.imshow(s,cmap='gray');plt.title("Canal S")
plt.subplot(235);plt.imshow(v,cmap='gray');plt.title("Canal V")
plt.subplot(236);plt.imshow(img_NZ_rgb);plt.title("Imagem original")



plt.show()
