#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:07:07 2024

@author: linuxu
"""

from skimage import io
from skimage.util import random_noise
import numpy as np
import glob
import os

def add_gaussian_noise(image, var):
    """Add Gaussian noise to an image."""
    noisy_image = random_noise(image, mode='gaussian', var=var)
    # Convert the noisy image to uint8
    noisy_image = (255 * noisy_image).astype(np.uint8)
    return noisy_image

# Read the image
png_files = glob.glob(os.path.join('/home/linuxu/Desktop/project_dSRVAE/valid/noisy/DIV2K_valid_LR_bicubic_X8', '*.png'))

# Define noise levels
noise_levels = [0.01, 0.05, 0.1, 0.2]

# Add noise at different levels and save the images
for var in noise_levels:
    for img in png_files:
        image = io.imread(img)
        noisy_image = add_gaussian_noise(image, var)
        img_name = img.split('/')[-1]
        filename = f'/home/linuxu/Desktop/project_dSRVAE/valid/noisy/DIV2K_valid_LR_bicubic_X8_{var}/{img_name}_noisy_image_var_{var}.png'
        io.imsave(filename, noisy_image)
        print(f'Saved {filename}')
        
        