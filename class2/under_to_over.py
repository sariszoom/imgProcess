import cv2 as cv
import numpy as np

img_input = cv.imread("imgProcess/class2/img/under.jpg", cv.IMREAD_GRAYSCALE)

# apply intensity transformation
img_output = np.log(img_input)

# scaling img intensity 0-255
img_max = np.max(img_output)
img_output = img_output * (255 / img_max)

# specify data type
img_output = np.array(img_output, dtype=np.uint8)

# save images
cv.imwrite("imgProcess/class2/img/under_to_over_input.png", img_input)
cv.imwrite("imgProcess/class2/img/under_to_over_output.png", img_output)