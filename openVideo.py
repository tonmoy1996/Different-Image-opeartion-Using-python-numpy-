import cv2
import time

cap=cv2.VideoCapture("myvideo.mp4")


if cap.isOpened()==False:
    print("Error Opening This File.. Try again")

while cap.isOpened():

    ret,frame=cap.read()

    if ret==True:


        time.sleep(1/20)
        cv2.imshow("Frame",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
    else:
        break;

cap.release()

cv2.destroyAllWindows()
