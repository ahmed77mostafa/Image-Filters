import cv2

gray_image = cv2.imread('Images/football-stadium-3404535_1280.jpg', cv2.IMREAD_GRAYSCALE)
equalized_image = cv2.equalizeHist(gray_image)

cv2.imshow('Original image', gray_image)
cv2.imshow('Equalized image', equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
