
import math
import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
 
# Initialize the Videoq
 
# Create the color Finder object
myColorFinder = ColorFinder(True)
hsvVals = 'red'
 
while True:
    img = cv2.imread(r"C:\Users\alessandrini\Desktop\mo lo faccio io\reference.png")
    img = img[0:720, :]
 
    # Find the Color Ball
    imgColor, mask = myColorFinder.update(img, hsvVals)
 
    press=cv2.waitKey(1)
    if press==ord("q"):
        break
        
    # Display
    img = cv2.resize(img, (0, 0), None, 0.7, 0.7)
    cv2.imshow("Imagje", imgColor)
    cv2.waitKey(1)