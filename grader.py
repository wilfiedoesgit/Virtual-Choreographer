from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import cv2   
import numpy as np
from BTCP import *
import works

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")
args = vars(ap.parse_args())

#distance formula to gauge difficulty(smaller distance) as well as performance
def distance(x1,x2):
    if abs(x1-x2) < 50:
        return True
    else:
        return False



#considers x and y components of the rectangles
def grader(cap,video):
    cap = cv2.VideoCapture(args['video'])
    test = track(cap, args['video'])
    
    while True:
        user_answer = input("1Million1,1Million2, or 1Million3")
        if user_answer == '1Million1':
            answer_key = works.Milpart1
            break
        elif user_answer == '1Million2':
            answer_key = works.Milpart2
            break
        elif user_answer == '1Million3':
            answer_key = works.Milpart3
            break
    
          
    red_answer = set(answer_key[0][0])
    blue_answer = set(answer_key[1][0])
    yellow_answer = set(answer_key[2][0])
    green_answer = set(answer_key[3][0])

    red_test = set(test[0][0])
    blue_test= set(test[1][0])
    yellow_test= set(test[2][0])
    green_test= set (test[3][0])
    
    #considers distance for both x and y
    count = 0
    for i in red_test:
        for j in red_answer:
            if distance(i[0],j[0]) or distance(i[1],j[1]):
                count += 1
    for i in blue_test:
        for j in blue_answer:
            if distance(i[0],j[0]) or distance(i[1],j[1]):    
                count += 1
    for i in yellow_test:
        for j in yellow_answer:
            if distance(i[0],j[0]) or distance(i[1],j[1]):    
                count += 1
    for i in green_test:
        for j in green_answer:
            if distance(i[0],j[0]) or distance(i[1],j[1]):
                count += 1

    #calculates percentage of how well the user did            
    total_answer_lines = ((len(answer_key[0])+len(answer_key[1])+len(answer_key[2]) + len(answer_key[3]))) 
    total_test_lines = ((len(test[0])+len(test[1])+len(test[2]) + len(test[3])))
    #count/average number of lines
    average = (total_test_lines +total_answer_lines)/2
    percentage = (count/average) 
    
    return percentage
grader(cap,args['video'])
