import albumentations as A

"""
Contains all the transforms that are applied to the images
You can add more to this pipeline, visit https://albumentations.ai/docs/ for more
"""
transform = A.Compose([
    A.HorizontalFlip(),
    A.VerticalFlip(),
    A.Rotate(),
    A.GaussianBlur()
])