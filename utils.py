import os
import sys
import cv2 as cv
import glob

def check_img_dir(dir):
    """
    Check if an image directory is valid
    Input: 
    - dir: directory to check

    Output:
    - True if directory is valid, False otherwise
    """
    if not os.path.isdir(dir):
        print('%s is not a valid directory.' % dir)
        sys.exit(1)

    return True

def check_dest_dir(dir):
    """
    Check if a destination directory exists, if not, create it
    """
    if not os.path.isdir(dir):
        os.mkdir(dir)

def read_images(img_dir, img_ext):
    """
    Read all images in a directory

    Input:
    - img_dir: directory to read images from

    Output:
    - list of image file paths
    """

    return glob.glob(f'{img_dir}/*{img_ext}', recursive=True)
