import time
import math
gravity = float(input("inserire  gravità (m/s*s) "))												
Half_gravity = gravity * 0.5 * -1																	
Ask = input("Accellerazione - periodo : ")
filo = float(input("inserisci lunghezza filo (m) "))
if Ask == ("accellerazione"):
	accelleration = gravity / filo * -1
	print("accellerazione", accelleration, "m/s*s")
if Ask == ("periodo"):
	periodo=6.28*(filo/gravity)**(1/2)
	print("periodo ",periodo , "s")