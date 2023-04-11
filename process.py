import os
import random

# Set the percentage of images to use for testing
test_percent = 5

# Set the path to the directory containing the images and annotations
data_dir = "data"

# Get a list of all the image file names in the directory
image_files = [os.path.join(data_dir, file_name) for file_name in os.listdir(data_dir) if file_name.endswith(".jpg")]

# Randomly shuffle the list of image file names
random.shuffle(image_files)

# Calculate the number of images to use for testing
num_test_images = round(len(image_files) * test_percent / 100)

# Write the file paths to the output files
with open(os.path.join(data_dir, "train.txt"), "w") as train_file, open(os.path.join(data_dir, "test.txt"), "w") as test_file:
    for i, file_path in enumerate(image_files):
        if i < num_test_images:
            test_file.write(file_path + "\n")
        else:
            train_file.write(file_path + "\n")
