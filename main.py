# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 22:53:36 2017

@author: Koji
"""

import cv2
import numpy as np

import modelmaker

filename = "test.jpg"
savefilename = "abc.ply"

img = cv2.imread(filename, 0)
cv2.imshow("img", img)
cv2.waitKey(-1)

modelmaker.createModel(savefilename, img)