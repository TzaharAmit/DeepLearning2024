#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:36:31 2024

@author: linuxu
"""

import shutil
import os
from distutils.dir_util import copy_tree

# copy file to test folder:
    
folder_name = 'DIV2K_valid_LR_bicubic_X8_0.2'

source = f'/home/linuxu/Desktop/project_dSRVAE/valid/noisy/{folder_name}'
destination = '/home/linuxu/Desktop/project_dSRVAE/dSRVAE/Test'
#os.makedirs(os.path.dirname(destination))
copy_tree(source, destination)

exec(open("test.py").read())

shutil.rmtree('/home/linuxu/Desktop/project_dSRVAE/dSRVAE/Test')
os.makedirs(os.path.dirname('/home/linuxu/Desktop/project_dSRVAE/dSRVAE/Test/'))

source = f'/home/linuxu/Desktop/project_dSRVAE/dSRVAE/Result'
destination = f'/home/linuxu/Desktop/project_dSRVAE/Results/final/original_models/noisy/{folder_name}/'
os.makedirs(os.path.dirname(destination))
copy_tree(source, destination)

shutil.rmtree('/home/linuxu/Desktop/project_dSRVAE/dSRVAE/Result')
os.makedirs(os.path.dirname('/home/linuxu/Desktop/project_dSRVAE/dSRVAE/Result/'))
