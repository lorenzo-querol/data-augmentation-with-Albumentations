import numpy as np
import cv2 as cv
import argparse
import os

from transforms import transform
from utils import check_img_dir, check_dest_dir, read_images

parser = argparse.ArgumentParser()
parser.add_argument('--i', help='Root directory of images to be augmented', required=True)
parser.add_argument('--o', help='Destination directory to save augmented images', default='./augmented_images')
parser.add_argument('--imgext', help='File extension of images, defaults to .jpg', default='.jpg')
parser.add_argument('--numaug', help='Number of augmented images to create from each original image, defaults to 5 per image', default=5)

args = parser.parse_args()
img_dir = args.i
num_aug = int(args.numaug)
img_ext = args.imgext
dest_dir = args.o

check_img_dir(img_dir)
check_dest_dir(dest_dir)

image_paths = read_images(img_dir)

augmented_images = []
for image_path in image_paths:
    image = cv.imread(image_path)
    rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    for i in range(num_aug):
        augmented_image = transform(image=image)["image"]
        
        filename = image_path.replace(img_ext, '') 
        filename = filename.split('/')[-1]
        filename = os.path.join(dest_dir, filename)
        augmented_filename = filename + ('_aug_%d' % (i+1)) + img_ext 

        augmented_image = cv.cvtColor(augmented_image, cv.COLOR_RGB2BGR) 
        cv.imwrite(augmented_filename, augmented_image)