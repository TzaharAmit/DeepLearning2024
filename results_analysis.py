# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:41:18 2024

@author: AmitTzahar
"""
import os
import cv2
import numpy as np
import pandas as pd
from skimage.metrics import structural_similarity as ssim
import plotly.io as pio
pio.renderers.default = 'browser'

def calculate_psnr(img1, img2):
    """
    Calculate the PSNR between two images.
    """
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:  # Means no difference between images
        return float('inf')
    max_pixel_value = 255.0
    psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))
    return psnr

def calculate_ssim(img1, img2):
    """
    Calculate the SSIM between two images.
    """
    # Convert images to grayscale if they are in color
    if len(img1.shape) == 3:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    if len(img2.shape) == 3:
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    ssim_value, _ = ssim(img1, img2, full=True)
    return ssim_value


def calculate_mse(img1, img2):
    """
    Calculate the Mean Squared Error (MSE) between two images.
    """
    # Ensure the images have the same dimensions
    if img1.shape != img2.shape:
        raise ValueError("Input images must have the same dimensions.")
    
    # Calculate the MSE
    mse_value = np.mean((img1 - img2) ** 2)
    return mse_value

def read_images_from_folder(folder_path):
    """
    Read all images from the specified folder.
    """
    images = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            img = cv2.imread(os.path.join(folder_path, filename))
            if img is not None:
                images.append(img)
    return images

def main(high_res_folder, super_res_folder):
    """
    Main function to calculate PSNR for all image pairs in the given folders.
    """
    high_res_images = read_images_from_folder(high_res_folder)
    super_res_images = read_images_from_folder(super_res_folder)

    if len(high_res_images) != len(super_res_images):
        print("Error: The number of high-resolution and super-resolved images do not match.")
        return

    psnr_values = []
    ssim_values = []
    mse_values = []
    for i in range(len(high_res_images)):
        resized_high_res_image = cv2.resize(high_res_images[i], (super_res_images[i].shape[1], super_res_images[i].shape[0]), interpolation=cv2.INTER_AREA)
        # psnr = calculate_psnr(resized_high_res_image, super_res_images[i])
        # psnr_values.append(psnr)
        ssim_val = calculate_ssim(resized_high_res_image, super_res_images[i])
        ssim_values.append(ssim_val)
        # mse = calculate_mse(resized_high_res_image, super_res_images[i])
        # mse_values.append(mse)
        # print(f"MSE: {mse:.2f}")
        # print(f"SSIM: {ssim:.4f}")
        # print(f"PSNR for image {i+1}: {psnr:.2f} dB")
    
    #average_psnr = np.mean(psnr_values)
    #print(f"Average PSNR: {average_psnr:.2f} dB")
    average_ssim = np.mean(ssim_values)
    # #print(f"Average SSIM: {average_ssim:.2f}")
    # average_mse = np.mean(mse_values)
    #print(f"Average MSE: {average_mse:.2f}")
    #res_df = pd.DataFrame(data={'data_type': [super_res_folder.split('/')[-1]], 'psnr': [average_psnr], 
     #                           'ssim': [average_ssim], 'mse': [average_mse]})
    res_df = pd.DataFrame(data={'data_type': [super_res_folder.split('/')[-1]], 'ssim': [average_ssim]})
    return res_df

if __name__ == "__main__":
    var_values = ['0.01', '0.05', '0.1', '0.2']
    high_res_folder = r"/home/linuxu/Desktop/project_dSRVAE/valid/noisy/DIV2K_valid_HR_0.2"
    high_res_folder_x8 = r"/home/linuxu/Desktop/project_dSRVAE/valid/noisy/X8_files_HR/DIV2K_valid_HR_0.2"
    folder_names = ['DIV2K_valid_LR_bicubic_X2_0.2', 'DIV2K_valid_LR_bicubic_X3_0.2', 'DIV2K_valid_LR_bicubic_X4_0.2', 'DIV2K_valid_LR_bicubic_X8_0.2']
    results = pd.DataFrame()
    for folder_name in folder_names:
        super_res_folder = f"/home/linuxu/Desktop/project_dSRVAE/Results/final/original_models/noisy/{folder_name}"
        if 'X8' in folder_name:
            res_df = main(high_res_folder_x8, super_res_folder)
        else:
            res_df = main(high_res_folder, super_res_folder)
        results = pd.concat([results, res_df])
    results.to_csv(r'/home/linuxu/Desktop/project_dSRVAE/Results/final/original_models/noisy/results_0.2_ssim.csv')

import plotly.graph_objects as go

# Data from the table
scales = ['x2', 'x3', 'x4', 'x8']
psnr_values = [33.04, 32.77, 31.96, 29.04]
ssim_values = [0.79, 0.78, 0.72, 0.36]
mse_values = [35.58, 37.69, 44.95, 86.65]

# PSNR plot
fig_psnr = go.Figure()
fig_psnr.add_trace(go.Scatter(x=scales, y=psnr_values,
                              mode='lines+markers+text',
                              name='PSNR',
                              line=dict(color='blue'),
                              text=[f"{val:.2f}" for val in psnr_values],
                              textposition="top center",
                              textfont=dict(size=20)))  # Enlarged text font
fig_psnr.update_layout(
    title=dict(text="PSNR Values dSRVAE", font=dict(size=30)),  # Enlarged title font
    xaxis=dict(title="Resolution", titlefont=dict(size=28), tickfont=dict(size=16)),  # Enlarged axis fonts
    yaxis=dict(title="PSNR (dB)", titlefont=dict(size=28), tickfont=dict(size=16)),  # Enlarged axis fonts
    hovermode="x unified"
)

# SSIM plot
fig_ssim = go.Figure()
fig_ssim.add_trace(go.Scatter(x=scales, y=ssim_values,
                              mode='lines+markers+text',
                              name='SSIM',
                              line=dict(color='green'),
                              text=[f"{val:.2f}" for val in ssim_values],
                              textposition="top center",
                              textfont=dict(size=20)))  # Enlarged text font
fig_ssim.update_layout(
    title=dict(text="SSIM Values dSRVAE", font=dict(size=30)),  # Enlarged title font
    xaxis=dict(title="Resolution", titlefont=dict(size=28), tickfont=dict(size=16)),  # Enlarged axis fonts
    yaxis=dict(title="SSIM", titlefont=dict(size=28), tickfont=dict(size=16)),  # Enlarged axis fonts
    hovermode="x unified"
)

# MSE plot
fig_mse = go.Figure()
fig_mse.add_trace(go.Scatter(x=scales, y=mse_values,
                             mode='lines+markers+text',
                             name='MSE',
                             line=dict(color='red'),
                             text=[f"{val:.2f}" for val in mse_values],
                             textposition="top center",
                             textfont=dict(size=20)))  # Enlarged text font
fig_mse.update_layout(
    title=dict(text="MSE Values dSRVAE", font=dict(size=30)),  # Enlarged title font
    xaxis=dict(title="Resolution", titlefont=dict(size=28), tickfont=dict(size=16)),  # Enlarged axis fonts
    yaxis=dict(title="MSE", titlefont=dict(size=28), tickfont=dict(size=16)),  # Enlarged axis fonts
    hovermode="x unified"
)

# Show plots
fig_psnr.show()
fig_ssim.show()
fig_mse.show()




