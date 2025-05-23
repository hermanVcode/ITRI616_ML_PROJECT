# For resizing the images from default 178*218 pixels to 128*128 while preserving facial proportions

# Step 1: Load image
# Step 2: Resize from 178*178 to 128*128

import os
import pandas as pd
import shutil
from PIL import Image

# Cleaning preprocessed folder
shutil.rmtree("data/img_align_preprocessed", ignore_errors=True)

images_to_process = int(20000) # Amount of images to process  

dir_processed_img = "data/img_align_preprocessed" # Path for storing processed images
os.makedirs(dir_processed_img, exist_ok=True) # Checks if the target directory exists, if not it will create it

dir_source_img = "data/img_align_celeba/img_align_celeba" # Path for the images

# Resizing entire image without cropping
for fname in os.listdir(dir_source_img)[:images_to_process]:
    if not fname.endswith('.jpg'):
        continue  # If the image is not in .jpg format it is skipped and not added to preprocessed image folder

    try:
        load_path = os.path.join(dir_source_img, fname)  # Load image path from the source directory
        # Step 1: Load image
        load_img = Image.open(load_path)  

        # Step 2: Resize image directly to 128x128
        resize_img = load_img.resize((128, 128))  # Resize entire image to 128x128
        resize_img.save(os.path.join(dir_processed_img, fname))  # Save resized image to preprocessed folder

    except Exception as e:
        print(f"Processing failed {fname}: {e}")  # Print exception if any image fails

