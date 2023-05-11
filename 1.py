import os
from PIL import Image, ImageFilter

input_folder = os.getcwd()
output_folder = os.path.join(input_folder, "1920X1080 auto image")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png",".JPG",".PNG",".JPEG",)):
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        if image.size == (1080, 1920):
            # Resize and blur the image
            # resized_image1 = image.resize((1080, 1920), Image.LANCZOS)
            resized_image1 = image.resize((650, 1080), Image.LANCZOS)
            blur = image.resize((1920, 1080), Image.LANCZOS)
            blurred_image1 = blur.filter(ImageFilter.GaussianBlur(30))

            # Paste the original image on top of the blurred image
            pos_x = (656)
            pos_y = (0)

            blurred_image1.paste(resized_image1,(pos_x,pos_y))

            # Save the resulting image
            output_path = os.path.join(output_folder, filename)
            blurred_image1.save(output_path)

        elif image.size != (1920,1080):
            # Resize and blur the image
            resized_image = image.resize((1920, 1080), Image.LANCZOS)
            blurred_image = resized_image.filter(ImageFilter.GaussianBlur(30))

            # Paste the original image on top of the blurred image
            pos_x = (1920 - image.size[0]) // 2
            pos_y = (1080 - image.size[1]) // 2
            blurred_image.paste(image, (pos_x, pos_y))

            # Save the resulting image
            output_path = os.path.join(output_folder, filename)
            blurred_image.save(output_path)

        

        else:
            # If the image is already 1920x1080, just copy it to the output folder
            output_path = os.path.join(output_folder, filename)
            image.save(output_path)

print ("Done!")