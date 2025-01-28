import cv2
import numpy as np

def cartoonify_image(image_path, output_path, alpha):
    # Read the input image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return

    # Resize for consistency
    img = cv2.resize(img, (500, 500))

    # Step 2: Convert to grayscale for edge detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_3ch = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    blended_image = cv2.addWeighted(gray_3ch, alpha, img, 1 - alpha, 0)


    # Save the result
    cv2.imwrite(output_path, gray)

    # Show the result
    cv2.imshow("Original Image", blended_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = "images/input.jpg"  # Replace with your input image path
output_path = "images/cartoonified.jpg"  # Replace with your desired output path
for i in range(3):
    cartoonify_image(image_path, output_path, i/5)
