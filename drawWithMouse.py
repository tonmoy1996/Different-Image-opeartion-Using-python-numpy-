
import cv2
import numpy as np


##############
def draw_Circle(event,x,y):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 50, color=(0, 255, 0), thickness=-1)


cv2.namedWindow(winname='draws')
cv2.setMouseCallback('draws',draw_Circle)



#######################


img=np.ones((512,512,3),np.int8)

while True:


    cv2.imshow("draws",img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break;


cv2.destroyAllWindows()


