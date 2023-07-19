import numpy as np
import cv2 as cv

#create empty
img = np.zeros([200,300],dtype = np.uint8)

for y in range( 75, 125):
  for x in range(50,250):
    img[y,x] = 255
    
#display img
cv.imshow('Drawing',img)

#wait
cv.waitKey(0)

#clean up
cv.destroyAllWindows()
