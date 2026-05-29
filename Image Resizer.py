import cv2
image = cv2.imread("Image3.jpeg")
if image is None:
    print("Image not found!")
else:
    sizes = {
        "Small": (200, 300),
        "Medium": (400, 600),
        "Large": (600, 900)
    }
    for name, size in sizes.items():
        resized_image = cv2.resize(image, size)
        cv2.imshow(f"{name} Image", resized_image)
        filename = f"{name.lower()}_image.jpg"
        cv2.imwrite(filename, resized_image)
        print(f"{filename} saved successfully!")
    cv2.waitKey(0)
    cv2.destroyAllWindows()