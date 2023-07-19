import numpy as np
import cv2 as cv

#read
img = cv.imread("class3/img/under2.jpg",cv.IMREAD_GRAYSCALE)

#create
filterSize = 15
kernel = np.ones((filterSize,filterSize),np.float32)/(filterSize**2)

#apply filter
output = cv.filter2D(img,-1,kernel,borderType=cv.BORDER_REFLECT)

cv.imwrite('class3/img/AverageInput.png',img)
cv.imwrite('class3/img/AverageOutput.png',output)