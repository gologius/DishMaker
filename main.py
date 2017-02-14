# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 22:53:36 2017

@author: Koji
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

import modelmaker

print "start"

filename = "test2.png"
savefilename = "abc.ply"
colorResolution = 8
medianFilterSize = 7

img = cv2.imread(filename, 0) #グレースケールで読み込み
img = cv2.medianBlur(img, medianFilterSize)
div = int(255 / colorResolution)
segment_img = img / div  #色の分解能を減らす

plt.imshow(img)
plt.imshow(segment_img)

modelmaker.createModel(savefilename, segment_img)

print "end"
