import numpy as np
import cv2
import os

pwd = os.getcwd()
# print("pwd:", f'{pwd}/example/.jpg')
imgname = "000000022192_ours"


img = cv2.imread(f'{pwd}/example/{imgname}.jpg') # ,0 
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# clipLimit颜色对比度的阈值
# titleGridSize进行像素均衡化的网格大小，即在多少网格下进行直方图的均衡化操作
clahe = cv2.createCLAHE(clipLimit=5,tileGridSize=(8,8))

#0 to 'L' channel, 1 to 'a' channel, and 2 to 'b' channel
img[:,:,0] = clahe.apply(img[:,:,0])


img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
print("input img shape=", img.shape)



cv2.imwrite(f'{imgname}.jpg', img)



