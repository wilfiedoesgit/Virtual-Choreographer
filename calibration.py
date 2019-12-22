from tkinter import *
import numpy as np
import cv2
from draw_over import *
from collections import deque
import numpy as np
import argparse
import imutils
import cv2



def calibrator():    
    
    web = cv2.VideoCapture(0)
    index = 0
    while(True):
        
        # Capture frame-by-frame
        ret, frame = web.read()
        frame = cv2.flip( frame, 1 )
        # Our operations on the frame come here
        # 
        # Display the resulting frame
        
        #Draws the rectangles for each body part
        frame = cv2.rectangle(frame,(719, 643), (748, 672),(225,0,0),2)
        cv2.putText(frame,"Right Foot",(719, 643),cv2.FONT_HERSHEY_SIMPLEX, 
            0.7, (0,0,255))
        frame = cv2.rectangle(frame,(746, 364), (771, 383),(0,0,255),2)
        cv2.putText(frame,"Right Hand",(746, 364),cv2.FONT_HERSHEY_SIMPLEX, 
            0.7, (0,0,255))
        frame = cv2.rectangle(frame,(543, 639), (578, 682),(0,255,0),2)
        cv2.putText(frame,"Left Foot",(543, 639),cv2.FONT_HERSHEY_SIMPLEX, 0.7, 
            (0,0,255))   
        frame = cv2.rectangle(frame,(527, 273), (560, 293),(104,161,166),2)
        cv2.putText(frame,"Left Hand",(527, 273),cv2.FONT_HERSHEY_SIMPLEX, 0.7, 
            (153,51,255))
        #controls speed of running through
        index += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        cv2.imshow("Calibration",frame)
    # When everything done, release the capture
    web.release()
    cv2.destroyAllWindows()