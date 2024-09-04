#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:51:15 2024

@author: linuxu
"""



m = torch.load('/home/linuxu/Desktop/project_dSRVAE_new/dSRVAE/models/VAE_SR.pth')
new_dict = {}
for key, value in m.items():
        new_dict['module.'+key] = value
print(new_dict.keys())
torch.save(new_dict, '/home/linuxu/Desktop/project_dSRVAE/dSRVAE/models/GAN_generator_5_module.pth')
