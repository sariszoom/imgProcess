import numpy as np
import cv2 as cv

#read
img = cv.imread("class3/img/under2.jpg",cv.IMREAD_GRAYSCALE)

#apply filter
ksize = (31,31)
sigmaX = 5.0
output = cv.GaussianBlur(img,ksize,sigmaX,borderType=cv.BORDER_REFLECT)

cv.imwrite('class3/img/GaussianInput.png',img)
cv.imwrite('class3/img/GaussianOutput.png',output)