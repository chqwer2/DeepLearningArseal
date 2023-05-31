
import numpy as np
import os
import scipy.io as sio


input_dir = "../../../../data/denoising/SIDD"

filepath = os.path.join(input_dir, 'ValidationNoisyBlocksSrgb.mat')
img = sio.loadmat(filepath)
Inoisy = np.float32(np.array(img['ValidationNoisyBlocksSrgb']))
Inoisy /=255.

filepath = os.path.join(input_dir, 'ValidationGtBlocksSrgb.mat')
img = sio.loadmat(filepath)
GT = np.float32(np.array(img['ValidationGtBlocksSrgb']))
GT /=255.



