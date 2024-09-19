import cv2
import os

# Paths
input_folder = '/storage/emulated/0/Download/'
output_folder = '/storage/emulated/0/OUTPUT/'

# Ensure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to create a pencil sketch
def create_pencil_sketch(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)

    # Apply Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # Blend the grayscale image with the blurred inverted image
    sketch_image = cv2.divide(gray_image, 255 - blurred_image, scale=256)

    # Save the pencil sketch image
    cv2.imwrite(output_path, sketch_image)

# Process all image files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpeg', '.jpg', '.png')):
        # Construct full file path
        file_path = os.path.join(input_folder, filename)

        # Construct output file path with the same name but without extension
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, f'{base_name}_sketch.jpg')

        # Create pencil sketch and save
        create_pencil_sketch(file_path, output_path)

print('Pencil sketch creation completed!')
