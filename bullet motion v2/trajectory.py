import math
import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
 
# Initialize the Video
catturato = cv2.VideoCapture(0)
rapp=602
catturato.set(cv2.CAP_PROP_FRAME_WIDTH,rapp)
catturato.set(cv2.CAP_PROP_FRAME_HEIGHT,1020)
 
# Create the color Finder object
colore = ColorFinder(False)
valori_colore = {'hmin': 0, 'smin': 157, 'vmin': 131, 'hmax': 21, 'smax': 255, 'vmax': 255}
 
# Variables
posListX, posListY = [], []
lista = [item for item in range(0, 1300)]
dove_cade = False

while True:
    success, img = catturato.read()
    img = img[0:1020, :] #quello è la Y
    # colore
    imgColor, maschera = colore.update(img, valori_colore)
    # dove sta lka pallla
    imgContours, location = cvzone.findContours(img, maschera)
    if location :
        posListX.append(location[0]['center'][0])
        posListY.append(location[0]['center'][1])
 
    if posListX:
        A, B, C = np.polyfit(posListX, posListY, 2)
        #creare punti
        for i, (posX, posY) in enumerate(zip(posListX, posListY)):
            pos = (posX, posY)
            cv2.circle(imgContours, pos, 5, (0, 255, 0))
            if i != 0:
                cv2.line(imgContours, pos, (posListX[i - 1], posListY[i - 1]), (0, 255, 0), 1)
        for x in lista:
            y = int(A *x*x + B * x + C) #equazione 2 grado
            cv2.circle(imgContours, (x, y), 1, (0, 0, 255), cv2.FILLED)#parabola
        #posizione finale reale
        a=2
        while len(posListX)==123 and a >1:
            posizionefittizia=posListX[122]
            posizione_effettiva=(1920*rapp)/posizionefittizia
            print("la posizione finale reale secondo dimenzioni reali immagine: ",posizione_effettiva,"pixel")
            a=-1
        if len(posListX) <5: #15 punti detectati sul immagine
            # Prediction
            a = A
            b = B
            c = C-385

            delta=float(b ** 2 - (4 * a * c))
            if delta > 0:
                radice=math.sqrt(delta)
                x = (int(-b +  radice/ (2 * a)))
                print(x)
                dove_cade = 300 < x < 450
        if dove_cade:
            cvzone.putTextRect(imgContours, "DENTRO", (10, 50), scale=2, thickness=5, colorR=(0, 200, 0), offset=20)
            print("daje zi è dentro")
        else:
            cvzone.putTextRect(imgContours, "FUORI", (10, 50),scale=2, thickness=5, colorR=(0, 0, 200), offset=20)
            print("é fUori zi ")
        press=cv2.waitKey(1)
        if press==ord("q"):
            break
    # Display
    cv2.imshow("rilevamento", imgContours)
    cv2.waitKey(1)