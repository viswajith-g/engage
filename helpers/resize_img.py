#!/usr/bin/env python3
from PIL import Image

path = "../images/counselling-career.png"

def resize_image(input_path, output_path, width, height):
    # Open the original image
    with Image.open(input_path) as img:
        # Resize the image
        resized_img = img.resize((width, height))
        # Save the resized image
        resized_img.save(output_path)
        print(f"Image saved to {output_path} with size {resized_img.size}")

# Example usage
resize_image(path, path, 200, 200)