import math
import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
 
# Initialize the Video
cap = cv2.VideoCapture(0)
rapp=602
cap.set(cv2.CAP_PROP_FRAME_WIDTH,rapp)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1020)
 
# Create the color Finder object
myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 0, 'smin': 191, 'vmin': 105, 'hmax': 12, 'smax': 255, 'vmax': 255}
 
# Variables
posListX, posListY = [], []
xList = [item for item in range(0, 1300)]
prediction = False

while True:
    success, img = cap.read()
    img = img[0:1020, :] #quello è la Y
    # find color of ball
    imgColor, mask = myColorFinder.update(img, hsvVals)
    # Find location of the Ball
    imgContours, contours = cvzone.findContours(img, mask)
    if contours :
        posListX.append(contours[0]['center'][0])
        posListY.append(contours[0]['center'][1])
 
    if posListX:
        # Polynomial Regression y = Ax^2 + Bx + C
        # Find the Coefficients
        A, B, C = np.polyfit(posListX, posListY, 2)
        #creare punti
        for x in xList:
            y = int(A *x*x + B * x + C) #equazione 2 grado
            cv2.circle(imgContours, (x, y), 1, (0, 0, 255), cv2.FILLED)#parabola
        #posizione finale reale
        a=2
        while len(posListX)==123 and a >1:
            posizionefittizia=posListX[122]
            posizione_effettiva=(1920*rapp)/posizionefittizia
            print("la posizione finale reale secondo dimenzioni reali immagine: ",posizione_effettiva,"pixel")
            a=-1
        if len(posListX) <7: #15 punti detectati sul immagine
            # Prediction
            a = A
            b = B
            c = C-385

            delta=float(b ** 2 - (4 * a * c))
            if delta > 0:
                radice=math.sqrt(delta)
                x = (int(-b +  radice/ (2 * a)))
                print(x)
                prediction = 350 < x < 445
        if prediction:
            cvzone.putTextRect(imgContours, "DENTRO", (50, 150),
                            scale=5, thickness=5, colorR=(0, 200, 0), offset=20)
        else:
            cvzone.putTextRect(imgContours, "FUORI", (50, 150),
                            scale=5, thickness=5, colorR=(0, 0, 200), offset=20)
        press=cv2.waitKey(1)
        if press==ord("q"):
            break
    # Display
    cv2.imshow("rilevamento", imgContours)
    cv2.waitKey(1)