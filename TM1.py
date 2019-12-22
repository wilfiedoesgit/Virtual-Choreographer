# events-example0.py
# Barebones timer, mouse, and keyboard events
#barebones animation start code from https://www.cs.cmu.edu/~112/notes/notes-animations.html
from tkinter import *
import numpy as np3e4
import cv2
from draw_over import *
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
from calibration import *
from PIL import Image
from PIL import ImageTk as itk
from sound import *
import works
from draw_part import *
from threading import Thread
from tkinter import filedialog
import tkinter
####################################
# customize these functions
####################################

import os
####################################
class Struct(object): pass
data = Struct()
############################
#from 15-112 website
import os
def listFiles(path):
    if (os.path.isdir(path) == False):
        # base case:  not a folder, but a file, so return singleton list with its path
        return [path]
    else:
        # recursive case: it's a folder, return list of all paths
        files = [ ]
        for filename in os.listdir(path):
            files += listFiles(path + "/" + filename)
        return files

# To test this, download and expand this zip file in the same directory
# as the Python file you are running:  sampleFiles.zip



def image_loader(data):
    data.yacht_image = itk.PhotoImage(Image.open("yacht.png"))
    # data.yacht_image = itk.PhotoImage(yacht)
    data.OneMillionImage = itk.PhotoImage(Image.open("1mil.jpg"))
    data.KPOPGROUP = itk.PhotoImage(Image.open("KPOPGROUP.jpg"))
    # data.HeartHand = itk.PhotoImage(Image.open("heart_hand.png"))
def init(data):
    data.level = 0
    data.width = 500
    data.height = 375
    image_loader(data)

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if event.keysym == "k":
        data.level = 2
    elif event.keysym == 'z':
        PrepixCall()
    elif event.keysym == 'x':
        web = cv2.VideoCapture('1Million1.mp4')
        Thread(target = play, kwargs = {'file':'1MilSound.wav'}).start()
        OneMillionCall(web)
        
    elif event.keysym == 'c':
        # Thread(target = play, kwargs = {'file':'MainSong.wav'}).start()
        calibrator()
    elif event.keysym == 'l':
        data.level = 5
    elif event.keysym == 'b':
        Thread(target = play, kwargs = {'file':'1MilP1.wav'}).start()
        draw_overlay(works.Milpart1)
    elif event.keysym == 's':
        data.level = 2
    elif event.keysym == 'y':
        data.level = 3

    elif event.keysym == 'n':
        Thread(target = play, kwargs = {'file':'M1P2.wav'}).start()
        draw_overlay(works.Milpart2)
        
    elif event.keysym == 'm':
        Thread(target = play, kwargs = {'file':'M1P3.wav'}).start()
        draw_overlay(works.Milpart3)
    elif event.keysym == 'q':
        Thread._destroy()
def timerFired(data):
    pass

def drawMainScreen(canvas,data):
    #What do you want to learn
    # play('MainSong.wav')
    canvas.create_rectangle(0,0,data.width,data.height, fill = "black")
    canvas.create_image(data.width/2,data.height/2, image = data.KPOPGROUP)
    canvas.create_text(data.width/2,data.height/10, text = "KPOP Dancethology",
        font = "Arial 30 bold", fill = 'white')
    canvas.create_text(data.width/2,9*data.height/10, text = "Press K", 
        font = "Arial 30 bold", fill = "white")
    
def drawSongList(canvas,data):#draws the song list
    canvas.create_rectangle(0,0,2*data.width,2*data.height, fill = 'pink')
    # canvas.create_image(data.width/2,data.height/2, image = data.HeartHand)
    canvas.create_text(data.width/2, 50, text = 
        'What song do you want do to learn?', font = "Arial 25 bold", 
        fill="Pink")
    # Current song list and future songs to come
    canvas.create_text(data.width/2, 3*data.height/8, 
        text = "박재범 Jay Park - YACHT (k) (Feat. Sik-K)",
         font = "Arial 20 bold", fill = "blue")
    canvas.create_text(data.width/2, data.height/2, text = 
        'Press Y for Yacht!', font = "Arial 20 bold", fill = "blue")
    canvas.create_text(data.width/2, 2.5*data.height/4, text = 
        'More songs coming!', font = "Arial 20 bold", fill = "red")
    canvas.create_text(data.width/2, 3.5*data.height/4, text =
        'Press C to calibrate', font = "Arial 15 bold", fill= 'purple')
    canvas.create_text(data.width/2, 3.8*data.height/4, text =
        'Press Q to exit calibration', font = "Arial 15 bold", fill= 'purple')
    canvas.create_text(data.width/2, data.height/6, text = 'Song List',
     font  = "Arial 50 bold" ,fill ="white")
    # groot = tkinter.Tk()
    # groot.withdraw()
    # file_path = filedialog.askopenfilename()
    # with open(file_path, 'r') as data:
    #     datalist = []
    #     exec('datalist = data.read()')
    #     print (datalist)
    #     draw_overlay(datalist)
    
        

def drawYachtScreen(canvas,data):
    canvas.create_image(data.width/2,data.height/2,image = data.yacht_image)
    canvas.create_text(data.width/4, data.height/4, text = "Prepix", 
        font = "Arial 30 bold", fill = "purple")
    canvas.create_text(data.width/4, 2*data.height/3, text = "Press Z", 
        font = "Arial 15 bold", fill = "yellow")
    canvas.create_text(data.width/4, 2.5*data.height/3, text = "Coming Soon!", 
        font = "Arial 15 bold", fill = "red")
    canvas.create_text(3*data.width/4, data.height/4, text = "1Million", 
        font = "Arial 30 bold", fill = "yellow")
    canvas.create_text(3*data.width/4, 2*data.height/3, text = "Press X", 
        font = "Arial 15 bold", fill = "purple")
    canvas.create_text(3*data.width/4, 2.5*data.height/3, text = "Press L to access parts", 
        font = "Arial 15 bold", fill = "purple")

def draw1Million(canvas, data):
    canvas.create_image(data.width/2,data.height/2, image = data.OneMillionImage)
    canvas.create_text(data.width/4, data.height/14, text = "Part 1", 
        font = "Arial 30 bold", fill = "purple")
    canvas.create_text(data.width/4, 2*data.height/13.9, text = "Press B", 
        font = "Arial 15 bold", fill = "yellow")
    canvas.create_text(2*data.width/4, data.height/14, text = "Part 2", 
        font = "Arial 30 bold", fill = "yellow")
    canvas.create_text(2*data.width/4, 2*data.height/13.95, text = "Press N", 
        font = "Arial 15 bold", fill = "purple")
    canvas.create_text(3*data.width/4, data.height/14, text = "Part 3", 
        font = "Arial 30 bold", fill = "purple")
    canvas.create_text(3*data.width/4, 2*data.height/13.9, text = "Press M", 
        font = "Arial 15 bold", fill = "yellow")

def PrepixCall():
    cap = cv2.VideoCapture('Prepix.mp4')
    
 
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
      print("Error opening video stream or file")
     
    # Read until video is completed
    while(cap.isOpened()):
    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
         
            # Display the resulting frame
            cv2.imshow('Frame',frame)
         
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
         
          # Break the loop
        else: 
            break
 
    # When everything done, release the video capture object
    cap.release()
 
    # Closes all the frames
    cv2.destroyAllWindows()
def OneMillionCall(web):
    cap = cv2.VideoCapture('1Mil.mp4')
    
 
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

 
# Read until video is completed
    while(cap.isOpened()):
    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
 
            # Display the resulting frame
            cv2.imshow('Frame',frame)
         
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
         
          # Break the loop
        else: 
            break
 
    # When everything done, release the video capture object
    cap.release()
 
    # Closes all the frames
    cv2.destroyAllWindows()
    
    draw_track(web)
def redrawAll(canvas, data):
    if data.level == 0:
        
        drawMainScreen(canvas, data)
    if data.level == 2:
        drawSongList(canvas,data)
    if data.level == 3:
        drawYachtScreen(canvas,data)
    if data.level == 5:
        draw1Million(canvas,data)
def callback():
    data.level = 3


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    # class Struct(object): pass
    # data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    # create the root and the canvas
    root = tkinter.Tk()
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
   
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(300,300)