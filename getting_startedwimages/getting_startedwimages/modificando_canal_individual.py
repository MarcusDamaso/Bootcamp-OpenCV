import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

img_NZ = cv2.imread("New_Zealand_Lake.jpg")
img_NZ_rgb = cv2.cvtColor(img_NZ, cv2.COLOR_BGR2RGB)
img_NZ_hsv = cv2.cvtColor(img_NZ, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(img_NZ_hsv)
novo_h = h + 10

""" obs: O canal HSV significa : H = Matiz, representa a cor em si, é imaginado como um círculo ou uma roda de cores 
S = saturação, representa a "pureza" da cor com 0 sendo cinza e o maxima uma cor super vibrante, V = Brilho, representa a clarida sendo 0 totalmente preto. Ou seja
quando adicionamos 10 ao canal da matiz um dado pixel na imagem por exemplo , se ele for vermelho vai ficar um pouco mais laranja/amarela , se for verde , um pouco mais 
Ciano ou azul e por ai vai."""

img_NZ_merged = cv2.merge((novo_h,s,v))
img_NZ_novoRBG = cv2.cvtColor(img_NZ_merged,cv2.COLOR_HSV2RGB)

plt.figure(figsize=[24,10])

plt.subplot(241);plt.imshow(img_NZ);plt.title("Imagem BGR Original")
plt.subplot(242);plt.imshow(img_NZ_merged);plt.title("Imagem HSV juntada com o novo canal h")
plt.subplot(243);plt.imshow(novo_h,cmap='gray');plt.title("Novo canal H")
plt.subplot(244);plt.imshow(s,cmap='gray');plt.title("Canal S")
plt.subplot(245);plt.imshow(v,cmap='gray');plt.title("Canal V")
plt.subplot(246);plt.imshow(img_NZ_rgb);plt.title("Imagem RGB original")
plt.subplot(247);plt.imshow(img_NZ_novoRBG);plt.title("Imagem RGB modiicada")



plt.show()
