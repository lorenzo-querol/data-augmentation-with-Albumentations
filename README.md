# data-augmentation-with-Albumentations
 
This repository is meant to show a minimum viable product of how to use [Albumentations](https://albumentations.ai/), a Python library used for data augmentation in Machine Learning or Deep Learning applications. 

## Requirements
```
albumentations == 1.3.0
numpy == 1.23.5
opencv_python_headless == 4.7.0.68
```

## Installation
Before running the script, install the necessary packages to run it using the following command:
```
pip install -r requirements.txt
```
This will install the packages mentioned beforehand in the requirements heading.

## Usage
To use the script, type the following command into your terminal/command prompt:
```
python augment.py [options]

options:
   --i         The directory to the images that will be augmented
   --o         The directory to where the augmented and original images will be saved (default is ./augmented_images)
   --ext       The extension of the images to augment (default is .JPG)
   --numaug    Number of augmented images to create from each original image (default is 5)
```
### Example
```
python augment.py --i test_images --numaug 10
```
This example will augment the folder `test_images` 10 times with varying combinations of transformations found in `transforms.py`.

## Customization
Users can alter the basic pipeline found in `transforms.py` to include more augmentations found in the library's [documentation](https://albumentations.ai/docs/).

```
transform = A.Compose([
    A.HorizontalFlip(),
    A.VerticalFlip(),
    A.Rotate(),
    A.GaussianBlur()
])
```

## Future Iterations
- [ ] Include support for object detection tasks (i.e., bounding box augmentation)


