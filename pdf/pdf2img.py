from pdf2image import pdf2image, convert_from_path
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as I


img = convert_from_path(r'C:\Users\calvchen\Downloads\daniel-moonasar-lesson-planning.pdf')

print(img)
# plt.imshow(img[0])
# plt.show()
for i,j in enumerate(img[7:9]):
    j.save(r'C:\Users\calvchen\Desktop\daniel-moonasar-lesson-planning{}.jpg'.format(i))





