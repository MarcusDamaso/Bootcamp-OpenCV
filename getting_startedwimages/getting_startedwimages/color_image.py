
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

coke_img = cv2.imread("coca-cola-logo.png",1)
print("image size is", coke_img.shape)
#o resultado do shape possui 3 dimensões porque é uma imagem RGB

print("Data type of image is ", coke_img.dtype)

plt.imshow(coke_img)
#a imagem vai aparecer azul, porque a ordem dos canais padr~çao do opencv nao é RGB e sim BGR!!
#então precisamos inverter aordem dos canais :

coke_img_channels_reversed = coke_img[:, :, ::-1] # coke_img é uma matriz numpy [altura , largura, profundidade] :: signifca percorres a lista toda e o step (-1) de traspra frente
plt.imshow(coke_img_channels_reversed)
plt.show()

print("")
