import numpy as np
import cv2 as cv

#create empty
filter = np.zeros([500,500],dtype = np.uint8)

ceta = int(45)
radius = int(200)

img = cv.imread("pug.jpg",cv.IMREAD_GRAYSCALE)

#สร้างเส้นตรง
for i in range (radius):
  x = int (i*np.cos(ceta))
  y = int (i*np.sin(ceta))
  filter[y,x] = 255

kernel = filter/np.sum(filter)

# print(filter)
# print(kernel)


conFilter = cv.filter2D(img,-1,kernel,borderType = cv.BORDER_REFLECT)

# display image
cv.imwrite('Draw Line.png', filter)
cv.imwrite('Convolution.png',conFilter)
cv.imshow('ConvolutionImg',conFilter)
cv.waitKey(0)
cv.destroyAllWindows()