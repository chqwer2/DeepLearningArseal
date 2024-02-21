import cv2

# Load a noisy image
noisy_image = cv2.imread('noisy_image.png', 0)  # Read the image in grayscale

# Denoise the image
denoised_image = cv2.fastNlMeansDenoising(noisy_image, h=10, templateWindowSize=7, searchWindowSize=21)

# Display the original and denoised images
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



