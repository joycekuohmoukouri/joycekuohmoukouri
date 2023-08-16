import cv2
from pathlib import Path

def cropp(input_directory, output_directory, image_names):
    # Ensure output directory exists
    Path(output_directory).mkdir(parents=True, exist_ok=True)

    # Dimensions for square cropping
    crop_size = 300

    # Loop through each image
    for image_name in image_names:
        # Read the image
        image_path = os.path.join(input_directory, image_name)
        img = cv2.imread(image_path)

        # Get the dimensions of the image
        height, width = img.shape[:2]

        # Calculate the cropping boundaries
        if width > height:
            left = (width - height) // 2
            right = left + height
            top = 0
            bottom = height
        else:
            top = (height - width) // 2
            bottom = top + width
            left = 0
            right = width

        # Crop the image
        cropped_img = img[top:bottom, left:right]

        # Resize the image to crop_size x crop_size
        cropped_img = cv2.resize(cropped_img, (crop_size, crop_size))

        # Save the cropped image
        output_path = os.path.join(output_directory, image_name)
        cv2.imwrite(output_path, cropped_img)

    print("Cropping and resizing complete.")
