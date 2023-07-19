import cv2 as cv

# Read img
img = cv.imread("imgProcess\class1\img\pug.jpg")
print("Data type of img (OpenCV): ",type(img))

#display
cv.imshow("Ex1 - imshow",img)

#save
cv.imwrite("out.png",img)

#wait
cv.waitKey(0)

#clean up
cv.destroyAllWindows()
