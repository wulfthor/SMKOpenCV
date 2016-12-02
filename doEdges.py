#!/usr/bin/python

from random import randint
import pdb
import sys
import time
import datetime
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

def inverte(name, imagem):
  imagem = (255-imagem)
  cv2.imwrite(name, imagem)

img = cv2.imread(sys.argv[1],0)
#imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(img,127,255,0)

#im2,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#res = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
namepart = "Z" + str(randint(0,100))
ts=time.time()
st=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')

#imP = Image.fromarray(res[1])
#im.save("your_file.jpeg")

printname = namepart + "_" + st + ".png"
img1 = cv2.imread(sys.argv[1])
h,w,bpp = np.shape(img1)
edges = cv2.Canny(img,100,200)
#cv2.imwrite('messigray.png',edges)
inverte(printname,edges)
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
