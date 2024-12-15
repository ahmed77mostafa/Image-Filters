import cv2
from skimage.restoration import  denoise_tv_chambolle

image = cv2.imread('Images/BASTANUK.jpg')
lamda = 0.3

denoised_image = denoise_tv_chambolle(image, weight = lamda)
cv2.imshow('Original Image',image)
cv2.imshow('Denoised Image',denoised_image)

cv2.waitKey(0)
cv2.destroyAllWindows()