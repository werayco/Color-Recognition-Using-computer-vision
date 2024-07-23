import cv2 as cv

cap = cv.VideoCapture(0)


while True:
    '''this code basically recognizes'''
    _,frame_bgr = cap.read()
    frame_hsv = cv.cvtColor(frame_bgr,cv.COLOR_BGR2HSV)
    cx,cy = int(frame_bgr.shape[1]//2),int(frame_bgr.shape[0]//2)
    cnt = frame_hsv[cx,cy]
    cv.circle(frame_bgr,(cx,cy),8,(0,255,0),1)
    hue = cnt[0]
    sat = cnt[1]
    val = cnt[2]


    if hue <5:
        cv.putText(frame_bgr,"Red",(100,100),0,1,(255,0,0),1)
    elif hue == 0:
        cv.putText(frame_bgr,"Black",(100,100),0,1,(255,0,0),1)
    elif hue<22:
        cv.putText(frame_bgr,"Orange",(100,100),0,1,(255,0,0),1)
    elif hue<33:
        cv.putText(frame_bgr,"Yellow",(100,100),0,1,(255,0,0),1)
    elif hue<78:
        cv.putText(frame_bgr,"Green",(100,100),0,1,(255,0,0),1)
    elif hue<131:
        cv.putText(frame_bgr,"Blue",(100,100),0,1,(255,0,0),1)
    elif hue<170:
        cv.putText(frame_bgr,"Violet",(100,100),0,1,(255,0,0),1)
    elif hue ==0 and sat == 0 and val == 0:
        cv.putText(frame_bgr,"Black",(100,100),0,1,(255,0,0),1)
    else:
        color=""
    print(cnt)
    # cv.putText(frame_bgr,color,(100,100),0,1,(255,0,0),1)
    cv.imshow("frame",frame_bgr)
    if cv.waitKey(1) & 0xFF == ord("x"):
        break

cap.release()
cv.destroyAllWindows()