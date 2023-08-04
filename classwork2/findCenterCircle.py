import cv2 as cv
import numpy as np

img = cv.imread("CircleObj.png")

#ทำให้ง่ายต่อการทำงาน
imgGray = cv.imread("CircleObj.png",cv.IMREAD_GRAYSCALE)

#ทำให้noiseเนียนเป็นสีเดียว
imgGray = cv.blur(imgGray,(5,5))

#find outline
outline = cv.Canny(imgGray,180,255)

#การวัดขนาดรูป
width = outline.shape[0]  #x
height = outline.shape[1] #y
radius = int(57) 
 

#draw circle around circle
for i in range (0,height,2):
  for j in range (0,width,2):
    dotOutline = outline[j,i]    
    if dotOutline == 255:
      
      cv.circle(img,(i,j),radius,(255,0,255),1) #flip y,x BGR ขนาดเส้น
      


# display image

cv.imshow('GrayImg',imgGray)
cv.imshow('OutlineImg',outline)
cv.imshow('Img',img)
cv.imwrite('findCenter.png', img)
cv.waitKey(0)
cv.destroyAllWindows()