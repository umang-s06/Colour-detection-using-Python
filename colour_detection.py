import pandas as pd
import cv2
import numpy as np

img = cv2.imread('color.jpeg')

index=['color','color_name','hex','R','G','B']
csv = pd.read_csv('colors.csv', names=index, header=None)

clicked=False
r=g=b=xpos=ypos=0

# mouse click function - helps in the process of double click
'''The function parameters have the event name, (x,y) coordinates of the mouse position, etc. 
Here, we check if the event is double-clicked then we calculate and set the r,g,b values 
along with x,y positions of the mouse.'''
def mouse_click(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global g,b,r,xpos,ypos,clicked
        clicked=True
        xpos=x
        ypos=y
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)

# color recognition function
#The function below will be called when you will double-click on an area of the image.
# It will return the name of the colour and the RGB values for that colour.
'''We have the r,g and b values. Now, we need another function which will return us the color name from RGB values. 
To get the color name, we calculate a distance(d) which tells us how close we are to color and 
choose the one having minimum distance.'''
def recognize_color(R,G,B):
    minimum=10000
