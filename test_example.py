# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import imquality.brisque as brisque
import PIL.Image

#path = 'path/to/image'
#img = PIL.Image.open(path)
#res = brisque.score(img)
#print('Score =', res)

import os
import glob
files = list(glob.glob(os.path.join("images",'*.*')))
print(files)
theimages = files

for x in theimages:
    img = PIL.Image.open(x)
    res = brisque.score(img);
    print('Score =',x, res)