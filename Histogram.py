import cv2

image = cv2.imread('Images/football-stadium-3404535_1280.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray_image)

cv2.imshow('Original image', image)
cv2.imshow('Equalized image', equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()