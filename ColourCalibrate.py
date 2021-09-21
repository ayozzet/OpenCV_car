import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
#print (cap)
while(True):
    ret, frame = cap.read()
    #print(frame.shape)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv,(15,15),0)
    

    low_yellow = np.array([20, 110, 180 ])
    high_yellow = np.array ([50, 200, 230])
    yellow_mask = cv2.inRange(blur, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

    plt.imshow(hsv)
    plt.show()
    #cv2.imshow("Detection", yellow_mask)
    #cv2.imshow("Mask", yellow)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
