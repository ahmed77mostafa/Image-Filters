import cv2

gray_image = cv2.imread('images/camel-train-3408458_1280.jpg',cv2.IMREAD_GRAYSCALE)
bgr_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
bgr_image[:, : ,0] = 100
bgr_image[:, : ,2] = 100

cv2.imshow('Gray Scale image 8-Bit' ,gray_image)
cv2.imshow('BGR image 24-bit' ,bgr_image)

cv2.waitKey(0)
cv2.destroyAllWindows()