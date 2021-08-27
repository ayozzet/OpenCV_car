import cv2

cap = cv2.VideoCapture(0)
#print (cap)
while(True):
    ret, frame = cap.read()
    otak = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow("HSV", otak)
    cv2.imshow("RGB", rgb)
    cv2.imshow("GRAY", gray)
    cv2.imshow("Original", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
