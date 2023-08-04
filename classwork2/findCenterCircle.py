import cv2 as cv
import numpy as np

img = cv.imread("CircleObj.png")

#ทำให้ง่ายต่อการทำงาน
imgGray = cv.imread("CircleObj.png",cv.IMREAD_GRAYSCALE)

#ทำให้noiseเนียนเป็นสีเดียว
imgGray = cv.blur(imgGray,(5,5))

#find outline
outline = cv.Canny(imgGray,180,255)



# for i in range (outline)


# display image
# cv.imwrite('Draw Line.png', filter)
# cv.imwrite('Convolution.png',conFilter)
cv.imshow('GrayImg',imgGray)
cv.imshow('OutlineImg',outline)
cv.waitKey(0)
cv.destroyAllWindows()