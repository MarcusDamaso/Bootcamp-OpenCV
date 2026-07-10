import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

img = cv2.imread("Apollo_11_Launch.jpg",1)
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#plt.imshow(img_rgb)
#plt.show()

#como fazer uma linha na imagem passando as coordenadas:
#criar uma cópia para preservar a imagem
imageLine = img_rgb.copy()

cv2.line(imageLine,(200,100),(400, 100), (255, 255, 0), thickness=5, lineType=cv2.LINE_AA);#_AA = antialiasing


#desenhando um circulo na imagem
cv2.circle(imageLine,(900,500), 100, (0,0,25),thickness = -2, lineType=cv2.LINE_AA);#qualque valor negativo de tyhicnkess preenche o circulo inteiro
cv2.rectangle(imageLine, (500,100), (700,600), (100,200,0),thickness=-10,lineType=cv2.LINE_AA);
plt.imshow(imageLine)
plt.show()

#inserindo texto na imagem

img_text = img_rgb.copy()
text = "Apollo 11 SAturn V Launch, July 16, 1969"
fontscale = 2.3
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (0,255,0)
fontThickness = 2

cv2.putText(img_text,text, (200,700), fontFace, fontscale, fontColor, fontThickness, cv2.LINE_AA);
plt.imshow(img_text)
plt.show()

