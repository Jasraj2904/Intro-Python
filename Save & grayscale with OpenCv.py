import cv2
image = cv2.imread('Image2.jpeg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resized_gray_image = cv2.resize(gray_image, (600, 400))
cv2.imshow('Processed Image', resized_gray_image)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('Processed_Image.jpeg', resized_gray_image)
    print("Image saved as 'Processed_Image.jpeg'")
else:
    print("Image not saved")
cv2.destroyAllWindows()
print(f"Resized grayscale image dimensions: {resized_gray_image.shape}")