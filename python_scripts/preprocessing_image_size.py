# For resizing the images from default 178*218 pixels to 128*128 while preserving facial proportions
# Remove background from images

# Step 1: Crop and then center image as square (178*178)
# Step 2: Resize from 178*178 to 128*128

import os
import pandas as pd
from PIL import Image

images_to_process = int(20000) # Amount of images to process  

dir_processed_img = "data/img_align_preprocessed" # Path for storing processed images
os.makedirs(dir_processed_img, exist_ok=True) # Checks if the target directory exists, if not it will create it

dir_source_img = "data/img_align_celeba" # Path for the images
face_bbox_csv = "data/list_bbox_celeba.csv" # Path for the .csv file containing the x,y coordinates of the face within the image

# Load the face_bbox_csv box data
face_bbox_df = pd.read_csv(face_bbox_csv, skiprows=1) # Skipping the first row containing the metadata
face_bbox_df.set_index('image_id', inplace=True)

# Cropping and resizing images, while removing background
for fname in face_bbox_df.index[:images_to_process]:
    if not fname.endswith('.jpg'):
        continue # If the image is not in .jpg format it is skipped and not added to preprocessed image folder
    try:
        
        load_path = os.path.join(dir_source_img, fname) # First load the images from the source directory
        load_img = Image.open(load_path) # load image into load_img
        bbox_img = face_bbox_df.loc[fname] # Get bounding box

        x_val = bbox_img['x_1'] # Get Top-left X coordinate of bounding box
        y_val = bbox_img['y_1'] # Get Top-left Y coordinate of bounding box
        width_val = bbox_img['width'] # Get Width of the bounding box
        height_val = bbox_img['height'] # Get Height of the bounding box

        # Bounding box centered on face, removing background
        bbox_side_length = max(width_val, height_val)
        x_val_center = x_val + width_val // 2
        y_val_center = y_val + height_val // 2
        x_val_sq1 = max(x_val_center - bbox_side_length // 2, 0)
        y_val_sq1 = max(y_val_center - bbox_side_length // 2, 0)
        x_val_sq2 = x_val_sq1 + bbox_side_length
        y_val_sq2 = y_val_sq1 + bbox_side_length

        # Step 1: Crop Image
        cropped_img = load_img.crop((x_val_sq1, y_val_sq1, x_val_sq2, y_val_sq2))

        # Step 2: Resize Cropped Image
        resize_img = cropped_img.resize((128, 128)) # Now resize_img contains the image as 128*128 size
        resize_img.save(os.path.join(dir_processed_img, fname))# Save image to preprocessed folder

    except Exception as e:
        print(f"Processing failed {fname}: {e}") # Exception will be printed

