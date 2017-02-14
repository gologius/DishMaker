# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 22:53:36 2017

@author: Koji
"""

import cv2
import numpy as np

import modelmaker


print "start"

filename = "test2.png"
savefilename = "abc.ply"
colorResolution = 16

img = cv2.imread(filename, 0)#グレースケールで読み込み
segment_img = np.clip(img, 0,colorResolution) * (255/colorResolution) #色の分解能を減らす

cv2.imshow("original", img)
cv2.imshow("segment", segment_img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

print "end"
modelmaker.createModel(savefilename, segment_img)
