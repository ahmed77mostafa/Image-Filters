import cv2

image = cv2.imread('Images/football-stadium-3404535_1280.jpg')
yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

yuv_image[: , : , 0] = cv2.equalizeHist(yuv_image[: , : , 0])
corrected_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)


cv2.imshow('Original image', image)
cv2.imshow('Equalized image', corrected_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
