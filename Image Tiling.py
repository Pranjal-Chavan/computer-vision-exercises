# import cv2 as cv
# import numpy as np

# img = cv.imread('PHOTOS/ex2.jpg')

# height, width = img.shape[:2]
# height1, width1 = height//2, width//2

# top_left     = img[0:height1     , 0:width1]
# top_right    = img[0:height1     , width1:width ]
# bottom_left  = img[height1:height, 0:width1]
# bottom_right = img[height1:height, width1:width]

# top = np.hstack((top_left, top_right))
# bottom = np.hstack((bottom_left, bottom_right))
# grid = np.vstack((top, bottom))

# cv.imshow('2 * 2 grid', grid)

# cv.waitKey(0)

import cv2 as cv
import numpy as np

img = cv.imread('PHOTOS/ex2.jpg')

height, width = img.shape[:2]
height1, width1 = height // 2, width // 2

# Split into 4 parts
top_left = img[0:height1, 0:width1]
top_right = img[0:height1, width1:width]
bottom_left = img[height1:height, 0:width1]
bottom_right = img[height1:height, width1:width]

# Adding the effects as simply grid does not show any change in grid therefore flipping and rotating the images
# Add effects to see the difference
top_left = cv.rotate(top_left, cv.ROTATE_180)
bottom_right = cv.flip(bottom_right, 1)  # flip horizontally

# Stack them
top = np.hstack((top_left, top_right))
bottom = np.hstack((bottom_left, bottom_right))
grid = np.vstack((top, bottom))

cv.imshow('2x2 Grid with Effects', grid)
cv.imwrite('output/2x2_grid_with_effects.jpg', grid)  # Save the grid image
cv.waitKey(0)

