import cv2

image = cv2.imread('Images/Wise man in library.jpg')
new_image = cv2.convertScaleAbs(image, alpha = 2, beta = 30)

cv2.imshow('Original Image', image)
cv2.imshow('New Image', new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()