import time
import math
gravity = float(input("inserire  gravità (m/s*s) "))												
Half_gravity = gravity * 0.5 * -1																	

ask=input("velocità angolare - frequenza - accellerazione centripeta ")
raggio = float(input("inserire raggio m "))
Periodo = float(input("inserire periodo s "))
if ask == ("velocità angolare"):
	angular_speed = (6.28 * raggio) / Periodo
	print("velocità angolare = ", angular_speed, "km/h")
		
if ask==("accellerazione centripeta"):
	angular_speed = (6.28 * raggio) / Periodo
	Accellerazione_centripeta= angular_speed * angular_speed / raggio
	print("accellerazione centripeta = ", Accellerazione_centripeta, "m/s*s")
		
if ask == ("frequenza"):
	frequenza=1/Periodo
	print("la frequenza è ", frequenza,"hz")