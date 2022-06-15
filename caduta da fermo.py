import time
import math
gravity = float(input("inserire  gravità (m/s*s) "))												
Half_gravity = gravity * 0.5 * -1																	
Height = float(input("inserire  altezza (m) "))
print("Tempo di Volo", (Height/(Half_gravity*-1))**(1/2), "secondi")
print("velocità finale", gravity * (Height/(Half_gravity*-1))**(1/2), "m/s")