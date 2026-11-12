import cv2
import numpy as np
c= cv2.VideoCapture(0)
c.set(3,160)
c.set(4,120)

while True:
    ret,frame=c.read()
    low= np.uint8([50,50,50])
    high= np.uint8([0,0,0])
    m= cv2.inRange(frame,high,low)

    conto,h= cv2.findContours(m,1,cv2.CHAIN_APPROX_NONE)
    if len(conto)>0:
        co= max(conto, key=cv2.contourArea)
        M= cv2.moments(co)
        if M["m00"] !=0:
            co_x=int(M['m10']/M['m00'])
            co_y=int(M['m01']/M['m00'])
            print("co_x: "+str(co_x)+"co_y: "+str(co_y))
            if co_x>= 120:
                print("Turn Left")
            elif co_x<120 and co_x>40:
                print("On track")
            elif co_x<=40:
                print("Turn Right")
            cv2.circle(frame,(co_x,co_y),5,(255,255,255),-1)
                

    cv2.drawContours(frame,co,-1,(0,255,0),1)

    cv2.imshow("mask,",m)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) and 0xff== ord('q'):
        break

c.release()
cv2.destroyAllWindows()