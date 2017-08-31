import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
      _,frame=cap.read()
      blurred = cv2.GaussianBlur(frame, (11, 11), 0)
      gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
      circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,2,20,param1=180,param2=100,minRadius=0,maxRadius=0)   
      
      if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0,:]: 
                    #draw the outer circle
                    cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
                    #draw the center of the circle
                    cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
        

      cv2.imshow('frame',frame)   
      key = cv2.waitKey(1) & 0xFF
      # if the 'q' key is pressed, stop the loop
      if key == ord("q"):
         break

cap.release()
cv2.destroyAllWindows()
