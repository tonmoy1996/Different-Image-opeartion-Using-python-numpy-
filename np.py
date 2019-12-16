import inline as inline
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img=Image.open("dog_backpack.png")
print(type(img))


# imshow(np.asarray(img))

#need to convert to numpy array

nparr=np.asarray(img)

copy=nparr.copy()

#R 0 G 1 B 2
copy[:,:,0]=0
copy[:,:,2]=0

print(copy)
plt.imshow(copy)

plt.show()





# img.show()
# import cv2
# import matplotlib.pyplot as plt
#
# im = cv2.imread('dog_backpack.png')
# im_resized = cv2.resize(im, (224, 224), interpolation=cv2.INTER_LINEAR)
#
# plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
# plt.show()