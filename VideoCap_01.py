import cv2

cap = cv2.VideoCapture(0)
#print (cap)
while(True):
    ret, frame = cap.read()

    cv2.imshow("Original", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
