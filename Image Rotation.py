import cv2
import imutils

image = cv2.imread('Images/BASTANUK.jpg')
rotated_image = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
rotated_image2 = imutils.rotate(image, 45)

cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Rotated Image 2', rotated_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()