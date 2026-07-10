import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

cb_img = cv2.imread("checkerboard_18x18.png",0)

""" plt.imshow(cb_img, cmap='gray')
print(cb_img)

print(cb_img[0,0]) #zero

print(cb_img[0,6]) """

cb_img_copy = cb_img.copy() #criar a cópia para nao perder a referencia original
cb_img_copy[2,2] = 140
cb_img_copy[2,3] = 200
cb_img_copy[3,2] = 140
cb_img_copy[3,3] = 200

plt.imshow(cb_img_copy,cmap='gray')
plt.show()
print(cb_img_copy)

