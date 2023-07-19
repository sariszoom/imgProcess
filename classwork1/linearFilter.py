import numpy as np
import cv2 as cv

#create empty
img = np.zeros([400,500],dtype = np.uint8)

p1 = (100,10)
p2 = (10,100)

cv.circle(img, p1, 1, 255, -1) 
cv.circle(img, p2, 1, 255, -1) 


# display image
cv.imshow('Draw Line', img)
cv.waitKey(0)
cv.destroyAllWindows()