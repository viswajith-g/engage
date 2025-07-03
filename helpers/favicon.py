#!/usr/bin/env python3
from PIL import Image

# this snipped of code should convert an image of your choosing into a .ico file that will go on to become the favicon for your website

image_path = "../images/logo2.png"  # Replace with the path to your image file
ico_path = "../images/favicon.ico"  # Path to save the converted ICO file
image = Image.open(image_path)
image.save(ico_path, format="ICO")