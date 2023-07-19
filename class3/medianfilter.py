import numpy as np
import cv2 as cv

#read
img = cv.imread("class3/img/GaussianOutput.png",cv.IMREAD_GRAYSCALE)

#apply filter
output = cv.medianBlur(img,5)

cv.imwrite('class3/img/MedianInput.png',img)
cv.imwrite('class3/img/MedianOutput.png',output)