#!/usr/bin/python

import pdb
import cv2
import logging
import sys
import os.path
import json
import re
import pprint as pp
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

#KMS4498,http://cspic.smk.dk/globus/40412247/img0083.jpg

def doStat(inputFile): 
  f = open( inputFile, 'rU' )
  lines=f.readlines()

  for line in lines:
    lineSplit=line.split(',')
    url=lineSplit[1]
    outname=lineSplit[0]
    filePost=url.split("/")
    tmpfileLine='/'.join(filePost[3:])
    fileLine = '/mnt/cifs/Globus/' + tmpfileLine.rstrip()
    pdb.set_trace()

    try:
      img = cv2.imread(fileLine)
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

    except:
      logging.info("Err: " + line)
      continue

    outputFile= outname + ".json"
    fh=open(outputFile, 'w')
    tmpLine='[{"id":"' + outname + '", "hue_med": "'
    fh.write(tmpLine)
    fh.close()

def main():
  logging.basicConfig(filename='logs/thw.log',level=logging.DEBUG)
  inputFile=sys.argv[1]
  doStat(inputFile)

if __name__ == '__main__':
  main()
