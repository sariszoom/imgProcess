import cv2 as cv
import numpy as np
import random


#function วัดความเหมือนกันของภาพ
def compute_ssim(img1, img2):
    mean1 = np.mean(img1)
    mean2 = np.mean(img2)
    std1 = np.std(img1)
    std2 = np.std(img2)
    cov = np.cov(img1.flatten(), img2.flatten())[0, 1]

    c1 = (0.01 * 255) ** 2
    c2 = (0.03 * 255) ** 2

    ssim = (
        (2 * mean1 * mean2 + c1)
        * (2 * cov + c2)
        / ((mean1 ** 2 + mean2 ** 2 + c1) * (std1 ** 2 + std2 ** 2 + c2))
    )

    return ssim

img = cv.imread('golden.jpg', cv.IMREAD_GRAYSCALE)
imgOrigin = cv.imread('golden.jpg', cv.IMREAD_GRAYSCALE)

#ขนาดnoise
density_salt = 0.1
density_pepper = 0.1

# Set salt
number_of_white_pixel = int(density_salt * (img.shape[0] * img.shape[1]))
# print(number_of_white_pixel) 10% ของรูป
# print(img.shape[0]*img.shape[1]) 100% ของรูป

# Add salt
for i in range(number_of_white_pixel):
    x_coord = random.randint(0, img.shape[1] - 1) #img.shape[1] - 1 pixelท้ายสุด
    y_coord = random.randint(0, img.shape[0] - 1)
    img[y_coord, x_coord] = 255

# Set pepper
number_of_black_pixel = int(density_pepper * (img.shape[0] * img.shape[1]))

# Add pepper
for i in range(number_of_black_pixel):
    x_coord = random.randint(0, img.shape[1] - 1)
    y_coord = random.randint(0, img.shape[0] - 1)
    img[y_coord, x_coord] = 0
    
output = img
maxSSIM = 0
blur = 1  #ต้องเป็นเลขแรก(คี่)
for i in range (1,19,2):
  #Add midblur for check (test)
  img = cv.medianBlur(img,i)
  compare = compute_ssim(imgOrigin,img)
  print(compare)
  
  #ดูค่า SSIM มากที่สุด
  if compare > maxSSIM:
    maxSSIM = compare
    blur = i
    
    print("Max SSIM : ", maxSSIM," Blur :", blur )
  
#Real midblur  
output = cv.medianBlur(output,blur)
    
cv.imshow('image_with_sp', output)
cv.imwrite('image_with_sp.png', output)
cv.waitKey(0)
cv.destroyAllWindows()





