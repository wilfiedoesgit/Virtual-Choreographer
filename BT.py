# https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
# concepts taken from the site
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
def track(cap):
    #takes a video file
    
    order = [[],[],[],[]]
    condition = True
    while condition:   
        _,img = cap.read()
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        #red range
        red_lower = np.array([136,87,111],np.uint8)
        red_upper = np.array([180,255,255],np.uint8)

        #blue range
        blue_lower = np.array([99,115,150],np.uint8)
        blue_upper = np.array([110,255,255],np.uint8)
        
        #yellow range
        yellow_lower = np.array([22,60,200],np.uint8)
        yellow_upper = np.array([60,255,255],np.uint8)

        #green range
        green_lower = np.array((29, 86, 6), np.uint8)
        green_higher = np.array((64, 255, 255), np.uint8)

        #finding the range of red,blue and yellow color in the image
        red = cv2.inRange(hsv, red_lower, red_upper)
        blue = cv2.inRange(hsv,blue_lower,blue_upper)
        yellow = cv2.inRange(hsv,yellow_lower,yellow_upper)
        green = cv2.inRange(hsv,green_lower,green_higher)

        #Morphological transformation, Dilation     
        kernal = np.ones((5 ,5), "uint8")

        red=cv2.dilate(red, kernal)
        res=cv2.bitwise_and(img, img, mask = red)

        blue=cv2.dilate(blue,kernal)
        res1=cv2.bitwise_and(img, img, mask = blue)

        yellow=cv2.dilate(yellow,kernal)
        res2=cv2.bitwise_and(img, img, mask = yellow)    

        green = cv2.dilate(green,kernal)
        res3 = cv2.bitwise_and(img,img,mask = green)

        _,contours,hierarchy =cv2.findContours(red,cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area>300):
                x,y,w,h = cv2.boundingRect(contour) 
                order[0].append([(x,y),(x+w,y+h)])
                print ("red",(x,y),(x+w,y+h))
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
                # cv2.putText(img,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
            # else:
            #     order[0].append(None)    
        #Tracking the Blue Color
        (_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area>300):
                x,y,w,h = cv2.boundingRect(contour) 
                order[1].append([(x,y),(x+w,y+h)])
                print ("blue",(x,y),(x+w,y+h))
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                # cv2.putText(img,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
            # else:
            #     order[1].append(None)
        #Tracking the yellow Color
        (_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area>300):
                x,y,w,h = cv2.boundingRect(contour)
                order[2].append([(x,y),(x+w,y+h)])
                print ("yellow",(x,y),(x+w,y+h))
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                # cv2.putText(img,"yellow  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))  
            # else:
            #     order[2].append(None)    
        (_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area>300):
                x,y,w,h = cv2.boundingRect(contour)
                order[3].append([(x,y),(x+w,y+h)])
                print ("green",(x,y),(x+w,y+h)) 
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            # else:
            #     order[3].append(None)    
            #cv2.imshow("Redcolour",red)
        #mirros it
        flipped_image = cv2.flip( img, 1 )
        cv2.imshow("Color Tracking",flipped_image)
        #cv2.imshow("red",res)  
        # if web and not _:
        #     break
        if cv2.waitKey(10) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break  
    return order