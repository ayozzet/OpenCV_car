import cv2

cap = cv2.VideoCapture(0)
#print (cap)
while(True):
    ret, frame = cap.read()

    #print(ret)
    print(frame)

cap.release()
cv2.destroyAllWindows()
