import cv2
import numpy as np
from matplotlib import pyplot as plt
im=cv2.imread('alarm.jpg')
row,column=im.shape[:2]
kernel_x=cv2.getGaussianKernel(column,200)
kernel_y=cv2.getGaussianKernel(row,200)
kernel=kernel_y*kernel_x.T
filter=255*kernel/np.linalg.norm(kernel)
vintage_im=np.copy(im)
for i in range (3):
    vintage_im[:,:,i]=vintage_im[:,:,i]*filter
plt.imshow(vintage_im)
plt.show()    