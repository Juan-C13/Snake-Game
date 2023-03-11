# Juan Clavijo - 2225709-3743
# Jose Miguel Fuertes - 2224623-3743

import pygame
import random
import time
from tkinter import *

# Ventana Ganador
gui = Tk()
gui.geometry("200x70")
gui.title('GANADOR')
gui.config(bg='black')
L0 = Label(gui, text=".", fg='black', bg='black')
L0.pack()


def mostrarpuntaje1(puntosJ1):
    letrero1 = score_font.render("Jugador 1:"+str(puntosJ1), True, blue)
    window.blit(letrero1, [80, 0])


def mostrarpuntaje2(puntosJ2):
    letrero2 = score_font.render("Jugador 2:"+str(puntosJ2), True, green)
    window.blit(letrero2, [520, 0])


pygame.init()
pygame.display.set_caption("Space Snake Game 1.3")
window = pygame.display.set_mode((800, 600))

score_font = pygame.font.SysFont("comicsansms", 35)

fondo = 40
background = (fondo, fondo, fondo)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
lightskyblue = (135, 206, 250)
blue = (135, 206, 250)
chartreuse = (127, 255, 0)

window.fill(black)
pygame.display.update()
clock = pygame.time.Clock()

continuar = True

# estas 2 lineas son para la musica, quitarlas si afecta al programa (además de otra línea al final)
pygame.mixer.music.load("Milky Ways.mp3", "mp3")
pygame.mixer.music.play(loops=999, start=0.0, fade_ms=0)

# jugador 1
x1 = random.randrange(0, 800, 10)
y1 = random.randrange(60, 600, 10)
pygame.draw.rect(window, blue, [x1, y1, 10, 10])

desplazamiento_X1 = 0
desplazamiento_Y1 = 0

# jugador 2
x2 = random.randrange(0, 800, 10)
y2 = random.randrange(60, 600, 10)
pygame.draw.rect(window, green, [x2, y2, 10, 10])

desplazamiento_X2 = 0
desplazamiento_Y2 = 0

# comida
x1_comida = random.randrange(0, 800, 10)
y1_comida = random.randrange(60, 600, 10)
pygame.draw.rect(window, red, [x1_comida, y1_comida, 10, 10])

puntosJ1 = 0
puntosJ2 = 0

mostrarpuntaje1(0)
mostrarpuntaje2(0)
pygame.display.update()

ritmo = 10

# fondo
coord_list = []
for i in range(150):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    coord_list.append([x, y])
z = 0

# eventos
while (continuar == True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuar = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                desplazamiento_X1 = -10
                desplazamiento_Y1 = 0
            elif event.key == pygame.K_RIGHT:
                desplazamiento_X1 = 10
                desplazamiento_Y1 = 0
            elif event.key == pygame.K_UP:
                desplazamiento_X1 = 0
                desplazamiento_Y1 = -10
            elif event.key == pygame.K_DOWN:
                desplazamiento_X1 = 0
                desplazamiento_Y1 = 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                desplazamiento_X2 = -10
                desplazamiento_Y2 = 0
            elif event.key == pygame.K_d:
                desplazamiento_X2 = 10
                desplazamiento_Y2 = 0
            elif event.key == pygame.K_w:
                desplazamiento_X2 = 0
                desplazamiento_Y2 = -10
            elif event.key == pygame.K_s:
                desplazamiento_X2 = 0
                desplazamiento_Y2 = 10

    x1 += desplazamiento_X1
    y1 += desplazamiento_Y1
    x2 += desplazamiento_X2
    y2 += desplazamiento_Y2

    pygame.draw.rect(window, blue, [x1, y1, 10, 10])
    pygame.draw.rect(window, green, [x2, y2, 10, 10])
    pygame.display.update()

    # el jugador 1 encuentra la comida:
    if (x1 == x1_comida and y1 == y1_comida):
        puntosJ1 += 1
        ritmo = ritmo+5
        pygame.draw.rect(window, blue, [x1, y1, 10, 10])
        mostrarpuntaje1(puntosJ1)

        x1_comida = random.randrange(0, 800, 10)
        y1_comida = random.randrange(60, 600, 10)

        pygame.draw.rect(window, red, [x1_comida, y1_comida, 10, 10])
        pygame.display.update()
        window.fill(black)

    # el jugador 2 encuentra la comida:
    if (x2 == x1_comida and y2 == y1_comida):
        puntosJ2 += 1
        ritmo = ritmo+5
        pygame.draw.rect(window, green, [x2, y2, 10, 10])
        mostrarpuntaje2(puntosJ2)

        x1_comida = random.randrange(0, 800, 10)
        y1_comida = random.randrange(60, 600, 10)

        pygame.draw.rect(window, red, [x1_comida, y1_comida, 10, 10])
        pygame.display.update()
        window.fill(black)

    # aumento de velocidad
    if (x1 == x1_comida and y1 == y1_comida):
        ritmo = ritmo+5
    if (x2 == x1_comida and y2 == y1_comida):
        ritmo = ritmo+5

    clock.tick(ritmo)

    # si algún jugador choca con los bordes:
    # si es el jugador 1:
    if (x1 < 0) or (x1 > 790) or (y1 < 0) or (y1 > 590):
        x1 = 400
        y1 = 300
        puntosJ1 += (-1)
        desplazamiento_X1 = 0
        desplazamiento_Y1 = 0

    # si es el jugador 2:
    if (x2 < 0) or (x2 > 790) or (y2 < 0) or (y2 > 590):
        x2 = 390
        y2 = 310
        puntosJ2 += (-1)
        desplazamiento_X2 = 0
        desplazamiento_Y2 = 0

    # Ganador
    if puntosJ1 == 5:

        LJ1 = Label(gui, text="Ganador: Jugador1",
                    fg='lightskyblue', bg='black')

        LJ1.pack()
        continuar = False

    elif puntosJ2 == 5:

        LJ2 = Label(gui, text="Ganador: Jugador 2",
                    fg='chartreuse', bg='black')

        LJ2.pack()
        continuar = False

    window.fill(black)

    # fondo
    for coordenada in coord_list:
        x = coordenada[0]
        y = coordenada[1]
        pygame.draw.circle(window, background, (x, y), 2)
        coordenada[1] += (-1)
        if coordenada[1] < 0:
            coordenada[1] = 600
    # fondo
    background = (fondo, fondo, fondo)
    if fondo == 10:
        z = 2
    if fondo == 40:
        z = -2
    fondo = fondo+z

    mostrarpuntaje1(puntosJ1)
    mostrarpuntaje2(puntosJ2)
    pygame.draw.rect(window, red, [x1_comida, y1_comida, 10, 10])

# esta es la otra linea para la musica, quitarla también si afecta al programa
pygame.mixer.music.unload()

if puntosJ1 != 5 and puntosJ2 != 5:
    L1 = Label(gui, text="No hay ganador", fg='white', bg='black')
    L1.pack()

gui.mainloop()
