import numpy as np
import cv2 as cv

#create empty image
img = np.zeros([200, 300, 3], dtype=np.uint8)

# draw circle
center = (150, 100)
radius = 40
color = (255, 255, 255)

thickness = cv.FILLED

cv.circle(img, center, radius, color, thickness)

# display image
cv.imshow('Drawing', img)

# wait
cv.waitKey(0)

# clean up
cv.destroyAllWindows()