import cv2
import numpy as np

import matplotlib.pyplot as plt


drawImage=np.zeros(shape=(500,500,3),dtype=np.int16)

font=cv2.FONT_ITALIC

cv2.putText(drawImage,"Hi....",org=(100,250),fontFace=font,fontScale=4,color=(0,0,255),thickness=5,lineType=cv2.LINE_AA)\

plt.imshow(drawImage)
plt.show()
