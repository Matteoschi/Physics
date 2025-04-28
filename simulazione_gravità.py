import pygame
import math
import csv
pygame.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GRAVITY MATTEO")

# Costanti
FPS = 500
r = 10000  # scala
COSTANTE_GRAVITY = 6.67430e-11 / r
BIANCO = (255, 255, 255)
NERO = (0, 0, 0)
GIALLO = (252, 223, 3)
RAGGIO_UFO = 5
MASSA_SOLE = 1.989e30 / r
MASSA_UFO = 5.972e24 / r

# scrivere dati sul file in utenti
with open("dati_simulazione.csv", mode='w', newline='') as file:
    writer = csv.writer(file , delimiter=";")
    writer.writerow(["ID", "Distanza_m", "Forza_N", "Accelerazione_m/s2", "Posizione_x_px", "Posizione_y_px", "Velocità_x_px/frame", "Velocità_y_px/frame" , "velocità orbitale"])

class Corpi:
    counter = 0
    def __init__(self, x, y, vel_x, vel_y, mass, color, raggio):
        self.x = x
        self.y = y
        self.velocità_x = vel_x
        self.velocità_y = vel_y
        self.raggio = raggio
        self.mass = mass
        self.color = color
        self.trajectory = []  
        self.id = Corpi.counter 
        Corpi.counter += 1

    def movimento(self, Stella):
        distanza = math.sqrt((self.x - Stella.x)**2 + (self.y - Stella.y)**2) * r
        
        Forza = (COSTANTE_GRAVITY * self.mass * Stella.mass) / distanza**2
        accelerazione = Forza / self.mass

        angolo = math.atan2(Stella.y - self.y, Stella.x - self.x)
        accelerazione_y = accelerazione * math.sin(angolo)
        accelerazione_x = accelerazione * math.cos(angolo)

        self.velocità_x += accelerazione_x
        self.velocità_y += accelerazione_y
        self.x += self.velocità_x
        self.y += self.velocità_y

        self.trajectory.append((self.x, self.y))  

        # scrivere terminale dati
        print(f"====== CORPO ID: {self.id} ======")
        print(f"Distanza dal Sole: {round(distanza, 2)} metri")
        print(f"Forza gravitazionale: {round(Forza, 2)} N")
        print(f"Accelerazione: {round(accelerazione, 5)} m/s²")
        print(f"Posizione: x = {round(self.x, 2)} px, y = {round(self.y, 2)} px")
        print(f"Velocità: vx = {round(self.velocità_x, 5)} px/f, vy = {round(self.velocità_y, 5)} px/f , velocità orbitale =  {math.sqrt(self.velocità_x**2+self.velocità_y**2)}")
        print("===============================\n")

        #scrivere dati simulazione
        with open("dati_simulazione.csv", mode='a', newline='') as file:
            writer = csv.writer(file , delimiter= ";")
            writer.writerow([
                self.id,
                round(distanza, 2),
                round(Forza, 2),
                round(accelerazione, 5),
                round(self.x, 2),
                round(self.y, 2),
                round(self.velocità_x, 5),
                round(self.velocità_y, 5),
                round(math.sqrt(self.velocità_x**2+self.velocità_y**2), 5)
            ])

    def draw(self):
        pygame.draw.circle(SCREEN, self.color, (int(self.x), int(self.y)), self.raggio)

        # traiettoria
        if len(self.trajectory) > 1:
            pygame.draw.lines(SCREEN, self.color, False, [(int(x), int(y)) for x, y in self.trajectory], 1)

def create_ship(location, mouse):
    t_x, t_y = location
    m_x, m_y = mouse
    vel_x = (m_x - t_x) / 100
    vel_y = (m_y - t_y) / 100
    obj = Corpi(x=t_x, y=t_y, vel_x=vel_x, vel_y=vel_y, mass=MASSA_UFO, color=BIANCO, raggio=RAGGIO_UFO)
    return obj

class Sole:
    def __init__(self, x, y, massa, color, raggio):
        self.x = x
        self.y = y
        self.mass = massa
        self.raggio = raggio
        self.color = color

    def draw(self):
        pygame.draw.circle(SCREEN, self.color, (self.x, self.y), self.raggio)

# Creazione del Sole al centro dello schermo
sole = Sole(WIDTH // 2, HEIGHT // 2, massa=MASSA_SOLE, color=GIALLO, raggio=40)

def main():
    running = True
    clock = pygame.time.Clock()
    objects = []
    temp_obj_position = None

    while running:
        clock.tick(FPS)
        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:  # uscire dalla pag
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_position:
                    obj = create_ship(temp_obj_position, mouse_position)
                    objects.append(obj)
                    temp_obj_position = None
                else:
                    temp_obj_position = mouse_position
                    print(f"pos x : {mouse_position[0]} , pos y {mouse_position[1]}")

        # Sfondo nero
        SCREEN.fill(NERO)

        # Disegna il Sole
        sole.draw()
        if temp_obj_position:
            pygame.draw.circle(SCREEN, BIANCO, (int(temp_obj_position[0]), int(temp_obj_position[1])), RAGGIO_UFO)
            pygame.draw.line(SCREEN, BIANCO, (int(temp_obj_position[0]), int(temp_obj_position[1])), mouse_position)

        # Disegna tutti i corpi (navicelle o pianeti)
        for obj in objects:
            obj.movimento(sole)
            obj.draw()

        # Aggiorna la finestra
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
