import  numpy as np
import matplotlib.pyplot as plt

import cv2


drawImage=np.zeros(shape=(500,500,3),dtype=np.int16)

# print(drawImage.shape)
# plt.imshow(drawImage*157)

# img=cv2.rectangle(drawImage,pt1=(10,10),pt2=(100,150),color=(255,0,0),thickness=10)

img=cv2.circle(drawImage,(250,250),radius=200,color=(100,100,240),thickness=-1)

print(img)
plt.imshow(img)

plt.show()