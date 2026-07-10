import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image

#esse código vai pegar colocar o background colorido na aprte branca do logo da coca cola

img_bgr = cv2.imread("coca-cola-logo .png")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
print(img_rgb.shape)

logo_w = img_rgb.shape[0]
logo_h = img_rgb.shape[1]

#precisamos deixar a imagem que vai entrar no lugar da parte branca do mesmo tamanho da imagem do logo

img_background_bgr = cv2.imread("checkerboard_color (1).png")
img_background_rgb = cv2.cvtColor(img_background_bgr, cv2.COLOR_BGR2RGB)

aspect_ration = logo_w / img_background_rgb.shape[1]
dim = (logo_w, int(img_background_rgb.shape[0] * aspect_ration))

img_background_rgb = cv2.resize(img_background_rgb, dim, interpolation=cv2.INTER_AREA)

plt.imshow(img_background_rgb)
print(img_background_rgb.shape)
plt.show()


#criar masks para o logo da coca cola
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

retval, img_mask = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
reval,inv_mask = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
plt.imshow(img_mask,cmap="gray")
print(img_mask.shape)

#obs, podemos usar a unção bitwise_not para criar uma mascara inversa

#criando o background colorido atras da mascara

img_background = cv2.bitwise_and(img_background_rgb, img_background_rgb, mask=img_mask)

img_foreground = cv2.bitwise_and(img_rgb, img_rgb, mask=inv_mask)
plt.imshow(img_foreground)

#agora somamos a imagem pra obter or esultado desejado ja que preto = 0 vamos ter aparte vermelha 

result = cv2.add(img_background, img_foreground)
plt.imshow(result)
cv2.imwrite("logoo_final.png",result)

plt.show()
print(retval)