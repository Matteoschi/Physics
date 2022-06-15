# Physics
In this repository dedicated to physics you will find various python codes to calculate  for example:
- [Bullet motion](#bullet-motion)
- [Centripetal acceleration](#centripetal-acceleration)
- [Pendulum](#pendulum)
- [How to calculate height](#how-to-calculate-height)
- [Free fall](#free-fall)





## Bullet-motion
<a name="bullet-motion"></a>
The code in which the motion of the projectile is calculated calculates how long and at what speed an object falls to the ground, neglecting friction.

- First the code asks what the gravity is and sets its half as a variable that will be used in moving forward with the calculations
```
gravity = float(input("inserire  gravità (m/s*s) "))												
Half_gravity = gravity * 0.5 * -1	
```
- It asks if you already have the speed and if you don't have it you need to enter the space and time, then the code will set a new variable called speed
```
if Ask_speed == ("no"):																			
	time = float(input("inserire intervallo di tempo per calcolare velocità (s) "))
	Space = float(input("inserire intervallo di spazio per calcolare velocità (m) "))
	Speed = Space / time
	print("velocità = ", Speed, "m/s", "    ", Speed * 3.6, "km/h")
else:
	Speed = float(input("inserire velocità m/s "))
	print("velocità = ", Speed, "m/s", "    ", Speed * 3.6, "km/h")
```
- then it asks for height in meters and the angle at which the object is thrown
```
Height = float(input("inserire  altezza (m) "))
Angle = float(input("inserire angolo (°) "))
```
- transform the angle into radians and set v0x and v0y as variables

```
angoloTrasformato = Angle / 57
angolo_Cos = math.cos(angoloTrasformato)
angolo_Sin = math.sin(angoloTrasformato)
V0x = Speed * angolo_Cos
V0y = Speed * angolo_Sin
```
- sets the delta of the second degree equation as variqable and his root
```
Delta = V0y*V0y - 4 * Height * Half_gravity
RadiceDelta = Delta**(1/2)
```
- calculates maximum height, flight time and final speed always thanks to the system between the uniformly accelerated rectilinear motion and the hourly wind
```
Fly_time = Numeratore / gravity * -1
print("Tempo di Volo", Fly_time, "secondi")
Distance_X = V0x * Fly_time
print("distanza = ", Distance_X, "metri")
half_time= Fly_time / 2
print("Altezza Massima", Half_gravity * half_time * half_time + V0y * half_time + Height, "metri")
print("velocità finale",  Speed+gravity*Fly_time, "m/s")
```

## Centripetal acceleration
<a name="centripetal-acceleration"></a>
- First the code asks what the gravity is and sets its half as a variable that will be used in moving forward with the calculations
```
gravity = float(input("inserire  gravità (m/s*s) "))												
Half_gravity = gravity * 0.5 * -1	
```
-the code ask which program do you want to run
```
ask=input("velocità angolare - frequenza - accellerazione centripeta ")
```
then you should tell him the radious and the period depends which program you need
```
raggio = float(input("inserire raggio m "))
Periodo = float(input("inserire periodo s "))
```
then the program makes simple calcules to calculate the argoment you need
```
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
```

## Pendulum
<a name="pendulum"></a>
-the code ask  gravity
```
gravity = float(input("inserire  gravità (m/s*s) "))												
Half_gravity = gravity * 0.5 * -1	
```
- it asks you the lengh of the wire and then it calculates the acceleration or the period as you need
```
Ask = input("Accellerazione - periodo : ")
filo = float(input("inserisci lunghezza filo (m) "))
if Ask == ("accellerazione"):
	accelleration = gravity / filo * -1
	print("accellerazione", accelleration, "m/s*s")
if Ask == ("periodo"):
	periodo=6.28*(filo/gravity)**(1/2)
	print("periodo ",periodo , "s")
```
## How to calculate height
<a name="how-to-calculate-height"></a>

```
gravity = float(input("inserire  gravità (m/s*s) "))												
Half_gravity = gravity * 0.5 * -1																	
Tempo = float(input("inserire tempo (s) "))
print(gravity/2*Tempo*Tempo," m altezza")
print(gravity*Tempo,"m/s velocità finale")
```

## free-fall
<a name="free-fall"></a>
- the free fall is a simplification of the motion of the projectile in fact we do not have the x axis having an angle of 90 degrees so we will not have to solve a second degree equation
```
Speed = float(input("inserire velocità m/s "))
print("velocità = ", Speed, "m/s", "    ", Speed * 3.6, "km/h")
Fly_time_caduta= ((Speed * -1) - (Speed * Speed - 4 * Half_gravity * Height) ** (1 / 2)) / gravity * -1
print("Tempo di volo", Fly_time_caduta, "secondi")
print("velocità finale", Speed+gravity*Fly_time_caduta)
```

## Authors

- [@Matteoschi](https://github.com/Matteoschi)
