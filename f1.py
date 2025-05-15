import cv2


input_image = cv2.imread('lena_ruido.png')


kernel_size = 5  
denoised_image = cv2.medianBlur(input_image, kernel_size)

cv2.imwrite('denoised_image.jpg', denoised_image)

cv2.imshow('Original Noisy Image', input_image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
