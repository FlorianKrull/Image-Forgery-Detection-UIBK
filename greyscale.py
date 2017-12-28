import cv2
import numpy as np 
import sys

if len(sys.argv) == 1:
  sys.exit("Usage: greyscale.py [Image] ")
  exit()
elif len(sys.argv) == 2:
  infilename = sys.argv[1]
else:
  sys.exit("Usage: greyscale.py [Image] ")
  exit() 

img = cv2.imread(infilename)

gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_'+str(img)+'.png',gray_image)

cv2.imshow('color-image',img)
cv2.imshow('gray image', gray_image)

cv2.waitKey(0)    

