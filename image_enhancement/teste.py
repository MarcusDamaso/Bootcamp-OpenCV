import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image

arr1 = np.array([200,250],dtype =np.uint8).reshape(-1,1)
arr2 = np.array([40,40],dtype =np.uint8).reshape(-1,1)
cu = arr1 + arr2
print(cu)