#importing modules
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import cv2   
import numpy as np
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")
args = vars(ap.parse_args())
#capturing video through webcam
if not args.get("video", False):
    cap = cv2.VideoCapture(0)

# otherwise, grab a reference to the video file
else:
    cap = cv2.VideoCapture(args["video"])


while(1):
    _, img = cap.read()
        
    #converting frame(img i.e BGR) to HSV (hue-saturation-value)

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #definig the range of red color
    red_lower=np.array([136,87,111],np.uint8)
    red_upper=np.array([180,255,255],np.uint8)

    #defining the Range of Blue color
    blue_lower=np.array([90,125,75],np.uint8)
    # blue_upper=np.array([110,255,255],np.uint8)
    #blue_lower=np.array([100,150,0],np.uint8)
    blue_upper=np.array([140,255,255],np.uint8)
    #defining the Range of yellow color
    yellow_lower=np.array([22,60,200],np.uint8)
    yellow_upper=np.array([60,255,255],np.uint8)
    green_lower = np.array([29, 86, 6], np.uint8)
    green_higher = np.array([64, 255, 255], np.uint8)

    #finding the range of red,blue and yellow color in the image
    red=cv2.inRange(hsv, red_lower, red_upper)
    blue=cv2.inRange(hsv,blue_lower,blue_upper)
    yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
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
    #Tracking the Red Color
    (_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            
            x,y,w,h = cv2.boundingRect(contour) 
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
            
    #Tracking the Blue Color
    (_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour) 
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),2)
            cv2.putText(img,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,225))

    #Tracking the yellow Color
    (_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour) 
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"yellow  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))  
            
    (_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
                # order[3].append([(x,y),(x+w,y+h)])
                # print ("green",(x,y),(x+w,y+h)) 
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            # else:
        #cv2.imshow("Redcolour",red)
    cv2.imshow("Color Tracking",img)
        #cv2.imshow("red",res)  
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break 