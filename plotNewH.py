#!/usr/bin/python

import sys
import os.path
import math
import pprint as pp
import scipy
from scipy import ndimage
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from scipy import misc
import scipy.misc
import cv2
import logging
import json
import re

#KMS4498,http://cspic.smk.dk/globus/40412247/img0083.jpg

def findLargestBin(inputarr): 
  collArr = ()
  for item in inputajrr:
    res=np.bincount()


def doStat(inputFile): 
  f = open( inputFile, 'rU' )
  lines=f.readlines()
  outdir='adstat'

  for line in lines:
    lineSplit=line.split(',')
    url=lineSplit[1]
    outname=lineSplit[0]
    filePost=url.split("/")
    tmpfileLine='/'.join(filePost[3:])
    fileLine = '/mnt/cifs/Globus/' + tmpfileLine.rstrip()

    try:
      if test == '1':
        img = cv2.imread(url.rstrip())
      else:
        #img = cv2.imread(fileLine)
        img = scipy.misc.imread(fileLine)
      b,g,r = cv2.split(img)
      img_rgb = cv2.merge([b,g,r])
      #array=np.asarray(img_rgb)
      array=np.asarray(img)
      arr=(array.astype(float))/255.0
      img_hsv = colors.rgb_to_hsv(arr[...,:3])

      thue=img_hsv[...,0].flatten()
      tsat=img_hsv[...,1].flatten()
      tval=img_hsv[...,2].flatten()
      hue=thue*360
      sat=tsat*100
      val=tval*100

      if test == '2':
        #plt.subplot(1,3,1)
        plt.hist(thue*360,bins=360,range=(0.0,360.0),histtype='stepfilled',color='r')
        plt.legend()
        #plt.subplot(1,3,2)
        #plt.hist(sat,bins=100,range=(0.0,100.0),histtype='stepfilled',color='g')
        #plt.legend()
        #plt.subplot(1,3,3)
        #plt.hist(val,bins=100,range=(0.0,100.0),histtype='stepfilled',color='b')
        #plt.legend()
        plt.show()


      maxHueArr = np.bincount(hue.flatten().astype(int))
      maxHue = int(np.ndarray.max(maxHueArr))
      maxHueIdx = int(np.ndarray.argmax(maxHueArr))
      maxSatArr = np.bincount(sat.flatten().astype(int))
      maxSat = int(np.ndarray.max(maxSatArr))
      maxSatIdx = int(np.ndarray.argmax(maxSatArr))
      maxValArr = np.bincount(val.flatten().astype(int))
      maxVal = int(np.ndarray.max(maxValArr))
      maxValIdx = int(np.ndarray.argmax(maxValArr))

      nHue = int(np.ndarray.mean(hue))
      mHue = int(np.median(hue))
      dHue = int(np.ndarray.std(hue))
      vHue = int(np.ndarray.var(hue))
      nSat = int(np.ndarray.mean(sat))
      mSat = int(np.median(sat))
      dSat = int(np.ndarray.std(sat))
      vSat = int(np.ndarray.var(sat))
      nVal = int(np.ndarray.mean(val))
      mVal = int(np.median(val))
      dVal = int(np.ndarray.std(val))
      vVal = int(np.ndarray.var(val))


    except:
      logging.info("Err: " + line)
      continue

    outputFile= outdir + "/" + outname + ".json"
    fh=open(outputFile, 'w')
    tmpLine='[{"id":"' + outname + '",'
    tmpLine+='"hue_med":{"set":' + str(mHue) + '},'
    tmpLine+='"hue_mea":{"set":' + str(nHue) + '},'
    tmpLine+='"hue_dev":{"set":' + str(dHue) + '},'
    tmpLine+='"hue_var":{"set":' + str(vHue) + '},'
    tmpLine+='"sat_med":{"set":' + str(nSat) + '},'
    tmpLine+='"sat_mea":{"set":' + str(mSat) + '},'
    tmpLine+='"sat_dev":{"set":' + str(dSat) + '},'
    tmpLine+='"sat_var":{"set":' + str(vSat) + '},'
    tmpLine+='"val_med":{"set":' + str(mVal) + '},'
    tmpLine+='"val_mea":{"set":' + str(nVal) + '},'
    tmpLine+='"val_dev":{"set":' + str(dVal) + '},'
    tmpLine+='"val_var":{"set":' + str(vVal) + '},'
    tmpLine+='"hue_max":{"set":' + str(maxHue) + '},'
    tmpLine+='"hue_max_bin":{"set":' + str(maxHueIdx) + '},'
    tmpLine+='"sat_max":{"set":' + str(maxSat) + '},'
    tmpLine+='"sat_max_bin":{"set":' + str(maxSatIdx) + '},'
    tmpLine+='"val_max":{"set":' + str(maxVal) + '},'
    tmpLine+='"val_max_bin":{"set":' + str(maxValIdx) + '}}]'
    fh.write(tmpLine)
    fh.close()

def main():
  logging.basicConfig(filename='logs/thw.log',level=logging.DEBUG)
  inputFile=sys.argv[1]
  global test
  test=sys.argv[2]
  doStat(inputFile)

if __name__ == '__main__':
  main()


