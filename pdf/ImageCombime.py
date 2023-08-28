import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image

w = 851
a1 = np.array(Image.open(r"C:\Users\calvchen\Pictures\1.png"))
a2 = np.array(Image.open(r"C:\Users\calvchen\Pictures\2.png").resize([w, 198], resample=Image.BICUBIC))
# a2 = Image.resize(size, resample=0)

# a3 = plt.imread(r"C:\Users\calvchen\Desktop\daniel-moonasar-lesson-planning2.jpg")
print(np.array(a1).shape, np.array(a2).shape)
# (727, 865, 3) (198, 854, 3)

# 2339,
a = np.concatenate([a1[:, :w-1],a2[:, 1:]],0)
plt.imshow(a)
plt.show()
plt.imsave(r"C:\Users\calvchen\Pictures\3.png", a)

