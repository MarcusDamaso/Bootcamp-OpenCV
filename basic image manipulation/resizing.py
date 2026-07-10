import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

img_NZ_bgr = cv2.imread("New_Zealand_Boat.jpg",cv2.IMREAD_COLOR)
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr,cv2.COLOR_BGR2RGB)



#como recortar a parte que tem o barco?


cropped_region = img_NZ_rgb[200:400, 300:600]#linhas de 200 até 400 e colunas de 300 até 600
#como dobrar o tamanho da imagem cropada

resized_cropped_region_2x = cv2.resize(cropped_region,None,fx=2, fy=2)
plt.imshow(resized_cropped_region_2x)

plt.show()

#outro método para mudar o tamanho das imagens;

desired_width = 100
desired_height = 200
dim = (desired_width,desired_height)

resized_cropped_region = cv2.resize(cropped_region, dsize=dim, interpolation=cv2.INTER_AREA)
plt.imshow(resized_cropped_region)
plt.show()

#resizing enquanto mantem as proporções da imagem
desired_width = 100
aspect_ratio = desired_width/ cropped_region.shape[1]
desired_height = int(cropped_region.shape[0] * aspect_ratio)
dim = (desired_width, desired_height)

resized_cropped_region = cv2.resize(cropped_region, dsize=dim, interpolation=cv2.INTER_AREA)
plt.imshow(resized_cropped_region)
plt.show()
