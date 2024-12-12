import cv2

image = cv2.imread('Images/camel-train-3408458_1280.jpg')
HSV_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow('Original Image', image)
cv2.imshow('RGB Image', RGB_image)
cv2.imshow('HSV Image', HSV_image)

cv2.waitKey(0)
cv2.destroyAllWindows()