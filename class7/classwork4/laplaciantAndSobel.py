import numpy as np
import cv2 as cv

def sobel_filter(image):
    # Sobel kernel แบบ Horizontal
    sobel_horizontal = np.array([[-1, -2, -1],
                                 [0, 0, 0],
                                 [1, 2, 1]])

    # Sobel kernel แบบ Vertical
    sobel_vertical = np.array([[-1, 0, 1],
                               [-2, 0, 2],
                               [-1, 0, 1]])

    # Filtering แบบ Horizontal และ Vertical
    filtered_horizontal = cv.filter2D(image, -1, sobel_horizontal)
    filtered_vertical = cv.filter2D(image, -1, sobel_vertical)

    return filtered_horizontal, filtered_vertical

# อ่านภาพเข้ามา
image = cv.imread('class7/img/catonnote.jpg', cv.IMREAD_GRAYSCALE)

# ใช้ Sobel Filter แบบ Horizontal และ Vertical กับภาพ
filtered_horizontal, filtered_vertical = sobel_filter(image)

# แสดงผลลัพธ์
cv.imwrite('class7/classwork4/sobelx.png', filtered_horizontal)
cv.imwrite('class7/classwork4/sobely.png',filtered_vertical)
cv.waitKey(0)
cv.destroyAllWindows()
