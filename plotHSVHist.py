#!/usr/bin/python

import cv2
import sys
import pprint as pp
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

#img = cv2.imread(sys.argv[1],0)
img = cv2.imread(sys.argv[1])
pr = int(sys.argv[2])
b,g,r = cv2.split(img)

if pr == 1:
	print " --- "
	for num in img:
		print num
		print "\n"
	print " --- "

rgb_img = cv2.merge([r,g,b])

if pr == 1:
	print " -II-- "
	for num in rgb_img:
		print num
		print "\n"
	print " --- "

#plt.imshow(rgb_img)
plt.imshow(img)
#plt.show

plt.hist(img.ravel(),256,[0,256]); plt.show()
hsv_image = cv2.cvtColor(rgb_img,cv2.COLOR_BGR2HSV)

hue, sat, val = hsv_image[:,:,0], hsv_image[:,:,1], hsv_image[:,:,2]
percHue = np.percentile(hue, 90)
pp.pprint(percHue)
maxHue = int(np.ndarray.max(hue))
nHue = int(np.ndarray.mean(hue))
dHue = int(np.ndarray.std(hue))
vHue = int(np.ndarray.var(hue))
nSat = int(np.ndarray.mean(sat))
dSat = int(np.ndarray.std(sat))
vSat = int(np.ndarray.var(sat))
nVal = int(np.ndarray.mean(val))
dVal = int(np.ndarray.std(val))
vVal = int(np.ndarray.var(val))
print " -Hue- "
print "Max " + str(maxHue)
print "M " + str(nHue)
print "D " + str(dHue)
print "V " + str(vHue)
print " -Sat- "
print "M " + str(nSat)
print "D " + str(dSat)
print "V " + str(vSat)
print " -Val- "
print "M " + str(nVal)
print "D " + str(dVal)
print "V " + str(vVal)
print " --- "
if pr == 1:
	for elem in hue:
		print elem

'''
plt.figure(figsize=(18,25))
plt.subplot(411)                             #plot in the first cell
plt.subplots_adjust(hspace=.5)
plt.title("Hue")
plt.hist(np.ndarray.flatten(hue), bins=256)
plt.show()
#plt.savefig(sys.argv[2] + '-hue.png')

plt.subplot(412)                             #plot in the second cell
plt.title("Saturation")
plt.hist(np.ndarray.flatten(sat), bins=256)
#plt.savefig(sys.argv[2] + '-sat.png')
plt.subplot(413)                             #plot in the third cell
plt.title("Luminosity Value")
plt.hist(np.ndarray.flatten(val), bins=256)
#plt.savefig(sys.argv[2] + '-lum.png')

plt.subplot(414)                             #plot in the third cell
plt.title("orig rgb")
color = ('b','g','r')

for i,col in enumerate(color):
	hist = cv2.calcHist([img],[i],None,[256],[0,256])
	plt.plot(hist,color=col)
	plt.xlim([0,256])
plt.savefig(sys.argv[2] + 'orig.png')
'''
import logging
import sys
import os.path
import json
import re
import PIL
from PIL import Image
from pprint import pprint

#KMS4498,http://cspic.smk.dk/globus/40412247/img0083.jpg

logging.basicConfig(filename='logs/thw.log',level=logging.DEBUG)

f = open( sys.argv[1], 'rU' )
lines=f.readlines()

for line in lines:
  lineSplit=line.split(',')
  url=lineSplit[1]
  filePost=url.split("/")
  tmpfileLine='/'.join(filePost[3:])
  fileLine = '/mnt/cifs/Globus/' + tmpfileLine.rstrip()

  try:
    image = Image.open(fileLine)
  except:
    logging.info("Err: " + line)
    continue

  w,h=image.size
  colors=image.getcolors(w*h)


  if len(colors) > 256:
    logging.info("C: " + line)
  else:
    logging.info("B: " + line)
