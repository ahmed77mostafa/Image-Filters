import cv2
import imutils

image = cv2.imread('Images/BASTANUK.jpg')
rotated_image = imutils.rotate(image, 45)

cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()