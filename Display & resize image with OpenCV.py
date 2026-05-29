import cv2
image = cv2.imread('Image.jpeg')
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', 600, 400)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"Image dimensions: {image.shape}")