import cv2 as cv

#read
img = cv.imread("imgProcess\class1\img\pug.jpg",cv.IMREAD_GRAYSCALE)

print("Data type of image(OpenCV):",type(img))
print("number of dimension:",img.ndim)
print("size of each dimension:",img.shape)
print("image height:",img.shape[0])
print("image width:",img.shape[1])

#display
cv.namedWindow('Example1 - imshow', cv.WINDOW_NORMAL)
cv.imshow("Example1 - imshow",img)

#wait
cv.waitKey(0)

#clean up
cv.destroyAllWindows()
