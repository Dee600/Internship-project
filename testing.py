# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from datetime import datetime
import time
#from __future__ import print_function
import sys
import numpy as np
import cv2
from PIL import Image

im = Image.open("C:\\Users\\Durgesh Reddiyar\\Desktop\\sayali\\sandbox\\res1.jpg")
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((204, 168))

print (r, g, b)
