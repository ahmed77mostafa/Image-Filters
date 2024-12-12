import cv2
import numpy as np

image = cv2.imread('Images/BASTANUK.jpg')

# rows = image.shape[0]
# cols = image.shape[1]

rows,cols = image.shape[:2]

t_x = 100
t_y = 50

translation_matrix = np.float32([
#   [x, y, transition value] treat x and y here as booleans
    [1, 0, t_x],
    [0, 1, t_y]
])

translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))

cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
