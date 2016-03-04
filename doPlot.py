#!/usr/bin/python

import numpy as np
import sys
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(sys.argv[1],1)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

b,g,r = cv2.split(img)
rgb_img = cv2.merge([r,g,b])
plt.imshow(rgb_img)
plt.show()

hsv_img = cv2.cvtColor(rgb_img,cv2.COLOR_BGR2HSV)
out_img = cv2.cvtColor(hsv_img,cv2.COLOR_HSV2BGR)
cv2.imwrite('mytest.png', hsv_img)
cv2.imwrite('mytestrgb.png', rgb_img)
cv2.imwrite('out_img.png', out_img)
cv2.imwrite('estrgb.png', img)
b,g,r = cv2.split(out_img)
out_rgb_img = cv2.merge([r,g,b])
cv2.imwrite('xout_img.png', out_rgb_img)

counter = 0
for item in hsv_img:
	counter = counter + 1
	if counter < 10:
		print item[0]

counter = 0
for item in rgb_img:
	counter = counter + 1
	if counter < 10:
		print item[0]

#plt.imshow(hsv_img)
#plt.show()
cv2.imshow('image',hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
