import cv2

cap = cv2.VideoCapture(0)
#print (cap)
while(True):
    ret, frame = cap.read()
    kabur = cv2.GaussianBlur(frame,(15,15),0)

    #edge1 = cv2.Canny(frame, 100, 200)
    edge2 = cv2.Canny(kabur, 100, 200)

    #cv2.imshow("Blur 1", edge1)
    cv2.imshow("Blur 2", edge2)
    #cv2.imshow("Original", frame)
    print(edge2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        #habis
cap.release()
cv2.destroyAllWindows()
