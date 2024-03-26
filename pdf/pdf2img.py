from pdf2image import pdf2image, convert_from_path
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as I


# pip install  pdf2image


img = convert_from_path(r'C:\Users\calvchen\Desktop\CSC\Letter of Recommendation.pdf')

print(img)

for i,j in enumerate(img[:]):
    j.save(r'C:\Users\calvchen\Desktop\CSC\Other Recommendation\Letter{}.jpg'.format(i))






