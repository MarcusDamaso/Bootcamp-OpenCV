
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys



img = cv2.imread("square.jpeg", 0)
img_fuzzy = cv2.imread("checkerboard_fuzzy_18x18.jpg", 0)

print ("Image size is: ", img.shape)
print("Data ype of image is ", img.dtype)

plt.imshow(img)

#o matplotlib utiliza um color map proprio para representar a imagem nao o grayscale entao temos que passar esse mapa pra ele
plt.imshow(img, cmap= 'gray')
plt.show()
plt.imshow(img_fuzzy, cmap = 'gray')
plt.show()