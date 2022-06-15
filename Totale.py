import time
import math
gravity = float(input("inserire  gravità (m/s*s) "))												
Half_gravity = gravity * 0.5 * -1																	
program=input("gravi - pendolo - moto circolare ")													
if program == ("gravi"):																			
	Type_program = input("Moto del proiettile(1) - Caduta da fermo(2) - Caduta libera(3) - Altezza(4) ")
	if Type_program == ("1"):
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
		
	if Type_program == ("2"):
		Height = float(input("inserire  altezza (m) "))
		print("Tempo di Volo", (Height/(Half_gravity*-1))**(1/2), "secondi")
		print("velocità finale", gravity * (Height/(Half_gravity*-1))**(1/2), "m/s")
		
	if Type_program == ("3"):
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
	if Type_program == ("4"):
		Tempo = float(input("inserire tempo (s) "))
		print(gravity/2*Tempo*Tempo," m altezza")
		print(gravity*Tempo,"m/s velocità finale")
		 

if program == ("pendolo"):
	Ask = input("Accellerazione - periodo : ")
	filo = float(input("inserisci lunghezza filo (m) "))
	if Ask == ("accellerazione"):
		accelleration = gravity / filo * -1
		print("accellerazione", accelleration, "m/s*s")

	if Ask == ("periodo"):
		periodo=6.28*(filo/gravity)**(1/2)
		print("periodo ",periodo , "s")

if program == ("moto circolare"):
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
	
time.sleep(10)
print("By Matteo")