import cv2

cap = cv2.VideoCapture(0)
#print (cap)
while(True):
    ret, frame = cap.read()
    kabur1 = cv2.GaussianBlur(frame,(15,15),0)
    kabur2 = cv2.GaussianBlur(frame,(101,101),0)

    cv2.imshow("Blur 1", kabur1)
    cv2.imshow("Blur 2", kabur2)
    cv2.imshow("Original", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
