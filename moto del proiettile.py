import time
import math
gravity = float(input("inserire  gravità (m/s*s) "))												
Half_gravity = gravity * 0.5 * -1																	
Ask_speed = (input("hai la velocità si/no "))													
if Ask_speed == ("no"):																			
	time = float(input("inserire intervallo di tempo per calcolare velocità (s) "))
	Space = float(input("inserire intervallo di spazio per calcolare velocità (m) "))
	Speed = Space / time
	print("velocità = ", Speed, "m/s", "    ", Speed * 3.6, "km/h")
else:
	Speed = float(input("inserire velocità m/s "))
	print("velocità = ", Speed, "m/s", "    ", Speed * 3.6, "km/h")
Height = float(input("inserire  altezza (m) "))
Angle = float(input("inserire angolo (°) "))
angoloTrasformato = Angle / 57
angolo_Cos = math.cos(angoloTrasformato)
angolo_Sin = math.sin(angoloTrasformato)
V0x = Speed * angolo_Cos
V0y = Speed * angolo_Sin
Delta = V0y*V0y - 4 * Height * Half_gravity
RadiceDelta = Delta**(1/2)
Numeratore = V0y * -1 - RadiceDelta
Fly_time = Numeratore / gravity * -1
print("Tempo di Volo", Fly_time, "secondi")
Distance_X = V0x * Fly_time
print("distanza = ", Distance_X, "metri")
half_time= Fly_time / 2
print("Altezza Massima", Half_gravity * half_time * half_time + V0y * half_time + Height, "metri")
print("velocità finale",  Speed+gravity*Fly_time, "m/s")
