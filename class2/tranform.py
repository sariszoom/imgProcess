import cv2 as cv
import numpy as np

img_in = cv.imread('imgProcess\class2\img\over.jpg',cv.IMREAD_GRAYSCALE)

#apply intensity tranform
gamma = 2
gamma_corrected = (img_in / 255)**gamma

#scaling output
gamma_corrected = gamma_corrected*255

#convert data
#overtounder
img_out = np.array(gamma_corrected, dtype = 'uint8')
#hdr
img_out = cv.equalizeHist(img_in)

#show
cv.imshow('power-law', img_out)

#save out
cv.imwrite('imgProcess\class2\img\gamma_input.png',img_in)
cv.imwrite('imgProcess\class2\img\gamma_output.png',img_out)