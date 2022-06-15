import time
import math
gravity = float(input("inserire  gravità (m/s*s) "))												
Half_gravity = gravity * 0.5 * -1																	
Tempo = float(input("inserire tempo (s) "))
print(gravity/2*Tempo*Tempo," m altezza")
print(gravity*Tempo,"m/s velocità finale")
