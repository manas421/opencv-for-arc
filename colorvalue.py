import cv2
import numpy as np
color = np.uint8([[[159,6,16 ]]])
hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
print hsv_color
