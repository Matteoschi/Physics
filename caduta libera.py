import time
import math
gravity = float(input("inserire  gravità (m/s*s) "))												
Half_gravity = gravity * 0.5 * -1																		

Height = float(input("inserire  altezza (m) "))
Ask_speed = (input("hai la velocità si/no "))													
if Ask_speed == ("no"):																			
    
	time = float(input("inserire intervallo di tempo per calcolare velocità (s) "))
	Space = float(input("inserire intervallo di spazio per calcolare velocità (m) "))

	Speed = Space / time
	print("velocità = ", Speed, "m/s", "    ", Speed * 3.6, "km/h")
else:
	Speed = float(input("inserire velocità m/s "))
	print("velocità = ", Speed, "m/s", "    ", Speed * 3.6, "km/h")
	Fly_time_caduta= ((Speed * -1) - (Speed * Speed - 4 * Half_gravity * Height) ** (1 / 2)) / gravity * -1
	print("Tempo di volo", Fly_time_caduta, "secondi")
	print("velocità finale", Speed+gravity*Fly_time_caduta)
