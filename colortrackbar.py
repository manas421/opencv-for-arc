import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('h:LOW','image',0,255,nothing)
cv2.createTrackbar('h:HIGH','image',0,255,nothing)
cv2.createTrackbar('s:LOW','image',0,255,nothing)
cv2.createTrackbar('s:HIGH','image',0,255,nothing)
cv2.createTrackbar('v:LOW','image',0,255,nothing)
cv2.createTrackbar('v:HIGH','image',0,255,nothing)
while True:
    _,frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos('h:LOW','image')
    hh=cv2.getTrackbarPos('h:HIGH','image')
    ls=cv2.getTrackbarPos('s:LOW','image')
    hs=cv2.getTrackbarPos('s:HIGH','image')
    lv=cv2.getTrackbarPos('v:LOW','image')
    hv=cv2.getTrackbarPos('v:HIGH','image')
    print(lh)

    lr=np.array([lh,ls,lv])
    ur=np.array([hh,hs,hv])

    mask = cv2.inRange(hsv,lr,ur)
    res = cv2.bitwise_and(frame ,frame,mask=mask)

    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k=cv2.waitKey(5)& 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
cap.release()
    
    
