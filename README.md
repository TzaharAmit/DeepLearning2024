# Image Super-Resolution Using Variational Autoencoders (VAE)
Amit Tzahar
Noam Tsfaty
Alon Gotlib
Ravit Shagan Damti

# Introduction
 Variational AutoEncoders (VAEs) represent a class of generative models that employ a probabilistic framework to encode input data into a latent space and subsequently decode it to synthesize new data. In the context of image super-resolution, VAEs are designed to map low-resolution images into a latent space that encapsulates crucial details, thereby facilitating the generation of high-resolution images. This approach enables VAEs to infer and reconstruct missing information, making them particularly effective in enhancing both the resolution and quality of images.
 
# Dependencies
    Python > 3.0
    OpenCV library
    Pytorch > 1.0
    NVIDIA GPU + CUDA
    pytorch-gan-metrics


# Implementation
# Perceptual Loss Approach:



# Unsupervised Generative Approach:
## 1. Test
---------------------------------------
1. Copy the test images to folder "Test" and run 
```sh
$ python test.py
```
The SR images will be created in folder "Result"

![our poster!](./images/poster_deep_learning.png)
