# image open using cv2  and destroy with pressed button
import cv2


img=cv2.imread("dog_backpack.png")

while True:
    cv2.imshow("Puppy",img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break;


cv2.destroyAllWindows()

