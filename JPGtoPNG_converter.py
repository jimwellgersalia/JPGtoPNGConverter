from PIL import Image
from sys import argv
import os

# Provide the relative path on the terminal the image folder and the folder you want to store the converted image
image_folder = argv[1]
output_folder = argv[2]


if not os.path.exists(output_folder):
    os.mkdir(output_folder)


for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png')
    print(f'{filename} is converted to png')
