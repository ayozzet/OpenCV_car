import numpy as np
import cv2
import math

#pixel columns n rows
lineCY = 220
lineCX = 320

def show_center():
    index = np.asarray(get[0])
    #print (index)
    if index.size > 0 :
        index_left = index[0]
        index_right = index[-1]
        #global center
        center = int(((index_right-index_left)/2)+index_left)
        #print(index_left, "--(",center,")--", index_right)
        cv2.line(frame, (center,lineCY),(center,lineCY-20),(0,0,255),2)
        return center
    #else:
        #print ("NO") #stop the ESC and try to reverse a few step back
    #return center
def drawText():
    if center is not None:
        #global val_from_line
        val_from_line = (center -lineCX)
        #print (center)
        #print (val_from_line)
        cv2.putText(frame, str(val_from_line), (center-20,lineCY-30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255), 2, cv2.LINE_AA)
        #cv2.putText(frame, (int(val_from_line), (20,20), cv2.FONT_HERSHEY_SIMPLEX, 12, (255), 1, cv2.LINE_AA)
        return val_from_line
    else:
        cv2.putText(frame, "UNDETECTED", (lineCX-105,lineCY-100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

def degree_angle():
    if (center is not None) and (lineCY is not None):
        cv2.line(frame, (320,480),(center, lineCY), (0,255,0),2)
        cv2.line(frame, (320, lineCY), (center, lineCY), (125, 125, 125), 2)
        adjacent = lineCY
        opposite = center -lineCX
        #print (opposite)
        theta = int (math.degrees(math.atan(opposite/adjacent)))
        thetaText = str(theta) + " degree"
        cv2.putText(frame, thetaText, (center-20,lineCY-50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (175,100), 2, cv2.LINE_AA)
        #print (int (theta))
        return theta

def servo():
    if degree is not None:
        #print (degree)
        if degree < 0:
            #steer left
            #print ("")
            valServo = int((-6*degree/5)+90)
            if valServo >= 150:
                outServo = 150
            else:
                outServo = valServo
            #print (valServo)
        elif degree > 0:
            #steer right
            #print ("")
            valServo = int((-4*degree/5)+90)
            if valServo <= 50:
                outServo = 50
            else:
                outServo = valServo
            #print (valServo)
        else:
            #straight
            #print ("Straight")
            valServo = int(degree)
            #print (valServo)
            outServo = valServo
        return outServo
    else:
        #reverse
        print ("REVERSE")

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

    edge = cv2.Canny(yellow, 100, 200)

    pix = np.asarray(edge)
    #print(edge.shape)
    get = np.where(pix[lineCY-1] == 255) # find 255 value at 480th rows
    print(get[0])
    center = show_center()
    val_from_center = drawText()
    #val_from_line = int(lineC - center)
    #print (val_from_center)
    #print (center)
    degree = degree_angle()
    #print (degree)
    Servo = servo()
    print(Servo)
    cv2.line(frame, (320,0),(320,480),(0,255,0),2) #reference line

    cv2.imshow("Original", frame)
    #cv2.imshow("HSV", hsv)
    #cv2.imshow("Mask", yellow_mask)
    #cv2.imshow("Detected", yellow)
    cv2.imshow("Canny", edge)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
=======
import numpy as np
import cv2
import math

#pixel columns n rows
lineCY = 220
lineCX = 320

def show_center():
    index = np.asarray(get[0])
    #print (index)
    if index.size > 0 :
        index_left = index[0]
        index_right = index[-1]
        #global center
        center = int(((index_right-index_left)/2)+index_left)
        #print(index_left, "--(",center,")--", index_right)
        cv2.line(frame, (center,lineCY),(center,lineCY-20),(0,0,255),2)
        return center
    #else:
        #print ("NO") #stop the ESC and try to reverse a few step back
    #return center
def drawText():
    if center is not None:
        #global val_from_line
        val_from_line = (center -lineCX)
        #print (center)
        #print (val_from_line)
        cv2.putText(frame, str(val_from_line), (center-20,lineCY-30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255), 2, cv2.LINE_AA)
        #cv2.putText(frame, (int(val_from_line), (20,20), cv2.FONT_HERSHEY_SIMPLEX, 12, (255), 1, cv2.LINE_AA)
        return val_from_line
    else:
        cv2.putText(frame, "UNDETECTED", (lineCX-105,lineCY-100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

def degree_angle():
    if (center is not None) and (lineCY is not None):
        cv2.line(frame, (320,480),(center, lineCY), (0,255,0),2)
        cv2.line(frame, (320, lineCY), (center, lineCY), (125, 125, 125), 2)
        adjacent = lineCY
        opposite = center -lineCX
        #print (opposite)
        theta = int (math.degrees(math.atan(opposite/adjacent)))
        thetaText = str(theta) + " degree"
        cv2.putText(frame, thetaText, (center-20,lineCY-50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (175,100), 2, cv2.LINE_AA)
        #print (int (theta))
        return theta

def servo():
    if degree is not None:
        #print (degree)
        if degree < 0:
            #steer left
            #print ("")
            valServo = int((-6*degree/5)+90)
            if valServo >= 150:
                outServo = 150
            else:
                outServo = valServo
            #print (valServo)
        elif degree > 0:
            #steer right
            #print ("")
            valServo = int((-4*degree/5)+90)
            if valServo <= 50:
                outServo = 50
            else:
                outServo = valServo
            #print (valServo)
        else:
            #straight
            #print ("Straight")
            valServo = int(degree)
            #print (valServo)
            outServo = valServo
        return outServo
    else:
        #reverse
        print ("REVERSE")

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

    edge = cv2.Canny(yellow, 100, 200)

    pix = np.asarray(edge)
    #print(edge.shape)
    get = np.where(pix[lineCY-1] == 255) # find 255 value at 480th rows
    print(get[0])
    center = show_center()
    val_from_center = drawText()
    #val_from_line = int(lineC - center)
    #print (val_from_center)
    #print (center)
    degree = degree_angle()
    #print (degree)
    Servo = servo()
    print(Servo)
    cv2.line(frame, (320,0),(320,480),(0,255,0),2) #reference line

    cv2.imshow("Original", frame)
    #cv2.imshow("HSV", hsv)
    #cv2.imshow("Mask", yellow_mask)
    #cv2.imshow("Detected", yellow)
    cv2.imshow("Canny", edge)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
>>>>>>> eea0e11d48e0ffd4a76dc123c9091477d1a5246b
