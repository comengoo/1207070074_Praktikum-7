#import library
import cv2
import numpy as np
from skimage import data
import matplotlib.pyplot as plt

#gray level slice
img = data.camera()

row, column = img.shape

img1 = np.zeros((row,column),dtype = 'uint8')
 
min_range = 10
max_range = 60

for i in range(row):
    for j in range(column):
        if img[i,j]>min_range and img[i,j]<max_range:
            img1[i,j] = 255
        else:
            img1[i,j] = 0

#plot image
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title("Citra Input")
ax[1].hist(img.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(img1, cmap=plt.cm.gray)
ax[2].set_title("Citra Output")
ax[3].hist(img1.ravel(), bins=256)
ax[3].set_title('Histogram Output')

plt.show()