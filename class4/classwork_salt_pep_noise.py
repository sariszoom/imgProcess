import cv2 as cv
import random

img = cv.imread('img/pug.jpg', cv.IMREAD_GRAYSCALE)

density_salt = 0.1
density_pepper = 0.1

# Set salt
number_of_white_pixel = int(density_salt * (img.shape[0] * img.shape[1]))

# Add salt
for i in range(number_of_white_pixel):
    x_coord = random.randint(0, img.shape[1] - 1)
    y_coord = random.randint(0, img.shape[0] - 1)
    img[y_coord, x_coord] = 255

# Set pepper
number_of_black_pixel = int(density_pepper * (img.shape[0] * img.shape[1]))

# Add pepper
for i in range(number_of_black_pixel):
    x_coord = random.randint(0, img.shape[1] - 1)
    y_coord = random.randint(0, img.shape[0] - 1)
    img[y_coord, x_coord] = 0
    
#Add midblur
img = cv.medianBlur(img,5)


cv.imwrite('image_with_sp.png', img)





