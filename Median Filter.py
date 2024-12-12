import cv2

image = cv2.imread('Images/OIP.jpg')
median_image = cv2.medianBlur(image, ksize = 5)

cv2.imshow('Original Image',image)
cv2.imshow('Median Filter Image', median_image)

cv2.imwrite('Images/Median Filter Image.jpg', median_image)

cv2.waitKey(0)
cv2.destroyAllWindows()