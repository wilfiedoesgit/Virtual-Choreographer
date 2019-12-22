import numpy as np
import cv2
from BT import *
from collections import deque
import numpy as np
import argparse
import imutils
import cv2

#analyzes a video
def draw_track(cap):    
    
    order =track(cap)
    print(order)
    web = cv2.VideoCapture(0)
    index = 0
    while(True):
        
        # Capture frame-by-frame
        ret, frame = web.read()

        # Our operations on the frame come here
        # 
        # Display the resulting frame
        #Draws the bounding rectangles for each body part
        if (index < len(order[0])) and order[0][index] != None:
            frame = cv2.rectangle(frame,order[0][index][0],
                order[0][index][1],(225,0,0),2)
        if (index < len(order[1])) and order[1][index] != None:
            frame = cv2.rectangle(frame,order[1][index][0],
                order[1][index][1],(0,0,255),2)
        if (index < len(order[2])) and order[2][index] != None:    
            frame = cv2.rectangle(frame,order[2][index][0],
                order[2][index][1],(0,255,0),2)
        if (index < len(order[3])) and order[3][index] != None:    
            frame = cv2.rectangle(frame,order[3][index][0],
                order[3][index][1],(153,51,255),2)
        index += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        flipped_image = cv2.flip( frame, 1 )
        cv2.imshow("Color Tracking",flipped_image)
    # When everything done, release the capture
    web.release()
    cv2.destroyAllWindows()


