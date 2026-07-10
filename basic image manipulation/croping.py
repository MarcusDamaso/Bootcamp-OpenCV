import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

img_NZ_bgr = cv2.imread("New_Zealand_Boat.jpg",cv2.IMREAD_COLOR)
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr,cv2.COLOR_BGR2RGB)


plt.imshow(img_NZ_rgb)

plt.show()
#como recortar a parte que tem o barco?


cropped_region = img_NZ_rgb[200:400, 300:600]#linhas de 200 até 400 e colunas de 300 até 600
plt.imshow(cropped_region)
plt.show()


