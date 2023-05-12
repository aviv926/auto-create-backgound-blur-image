import os
from PIL import Image, ImageFilter
import cv2

def process_image(image_path, output_folder):
    image = Image.open(image_path)
    width, height = image.size

    # Create a blurred background
    background = image.resize((1920, 1080), Image.LANCZOS)
    background = background.filter(ImageFilter.GaussianBlur(30))

    # Paste the original image onto the blurred background
    if width == 1080 and height == 1440:
        x_offset = (1920 - 1080) // 2
        y_offset = 0
    elif width == 1080 and height == 1920:
        # Resize the image to fit within 1920x1080 while maintaining aspect ratio
        resized_image = image.resize((607, 1080), Image.LANCZOS)
        x_offset = (1920 - 607) // 2
        y_offset = 0
    else:
        x_offset = (1920 - width) // 2
        y_offset = (1080 - height) // 2

    background.paste(resized_image if width == 1080 and height == 1920 else image, (x_offset, y_offset))

    # Save the processed image to the output folder
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    background.save(output_path)

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg','.JPG','.PNG','.JPEG')):
            image_path = os.path.join(input_folder, filename)
            process_image(image_path, output_folder)

input_folder = os.getcwd()
output_folder = os.path.join(input_folder, "1920X1080 auto image")

process_folder(input_folder, output_folder)

print("Done. Hope you found that helpful for you :P")
