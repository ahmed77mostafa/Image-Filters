import cv2

image = cv2.imread('Images/football-stadium-3404535_1280.jpg')

width,height = image.shape[:2]
new_width, new_height = int(width * 0.5), int(height * 0.5)

scaled_image = cv2.resize(image, (new_width, new_height))

cv2.imshow('Original Image', image)
cv2.imshow('Scaled Image', scaled_image)

cv2.waitKey(0)
cv2.destroyAllWindows()