
#Blend Image into one another using addWeighted Function
import cv2

import numpy as np
import matplotlib.pyplot  as plt

img1=cv2.imread("dog_backpack.png")
img2=cv2.imread("watermark_no_copy.png")


img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)


new_img1=cv2.resize(img1,(1200,1200))
new_img2=cv2.resize(img2,(1200,1200))


blend_Image=cv2.addWeighted(src1=new_img1,alpha=.5,src2=new_img2,beta=.5,gamma=0)


plt.imshow(blend_Image)
# plt.imshow(img2)
plt.show()