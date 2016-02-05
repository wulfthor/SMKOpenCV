#!/usr/bin/python

import cv2
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

#img = cv2.imread(sys.argv[1],0)
#plt.hist(img.ravel(),256,[0,256]); plt.show()
img = cv2.imread(sys.argv[1])
color = ('b','g','r')
for i,col in enumerate(color):
	hist = cv2.calcHist([img],[i],None,[256],[0,256])
	plt.plot(hist,color=col)
	plt.xlim([0,256])
plt.show()
plt.savefig(sys.argv[2] + '.png')

