#!/usr/bin/python

import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(sys.argv[1],0)
img1 = cv2.imread(sys.argv[1])
h,w,bpp = np.shape(img1)
edges = cv2.Canny(img,100,200)
he,we = np.shape(edges)
print(str(he) + " " + str(h))
print(str(we) + " " + str(w))
print(" " + str(bpp))

'''
for i in range(0,(h-1)): 
	print edges[i]

print " .. "
for i in range(0,(h-1)): 
	print img[i]

#for j in range(0,h):
#		print edges[i][j]


cv2.imshow('matrix',edges)
'''

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
