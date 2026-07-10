import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image

img_bgr = cv2.imread("New_Zealand_Coast.jpg",cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)

matrix1 = np.ones(img_rgb.shape) * .8
matrix2 = np.ones(img_rgb.shape) * 1.2

#obsd na multiplicação é necessario usar np.float64 para converter o tipo da imagem pra floar e ddps np.uint8 para trasnformar em int novamente

img_rgb_darker = np.uint8(cv2.multiply(np.float64(img_rgb), matrix1))
img_rgb_brighter = np.uint8(cv2.multiply(np.float64(img_rgb), matrix2))
#forma de contornar o "pixel estourado"
img_rgb_higher = np.uint8(np.clip(cv2.multiply(np.float64(img_rgb), matrix2),0,255))

plt.figure(figsize=[18,5])

plt.subplot(131); plt.imshow(img_rgb_darker); plt.title("Baixo contraste")
plt.subplot(132); plt.imshow(img_rgb);plt.title("Original")
plt.subplot(133); plt.imshow(img_rgb_higher); plt.title("Alto contraste")#a explosãoa contece pq ao multiplicarmos a matriz original por um valor >1 o pixel pode passar de 255

plt.show()