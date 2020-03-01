import sys
import os
from PIL import Image

# grab first and second arg with sys
if len(sys.argv) < 3:
    print("Please provide the original file and new directory to copy files to")
    exit(1)

originals, converted = sys.argv[1], sys.argv[2]

# check if new folder exists and create if not
if os.path.isdir(converted):
    print("New directory already exists...continuing")
else:
    print(f"Creating directory {converted}")
    os.mkdir(converted)

# loop through pokedex and convert to png
for file in os.listdir(originals):
    filename = os.path.splitext(file)[0]
    og_image = Image.open(f'{originals}/{file}')
    print(f'Converting {file} to png...')
    og_image.save(f'{converted}/{filename}.png', "png")
   

