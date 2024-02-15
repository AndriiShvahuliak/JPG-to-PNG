import sys
import os
from PIL import Image

# entering input and output folders
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# creating output folder if doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# looping through the input folder, converting images to PNG and saving them in the output folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename[0])
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print(f'{img} has been converted to png')
# testing
# nyama
# final testing(i hope)
