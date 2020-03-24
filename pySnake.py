# 2020 Quarantine python project
# A simple terminal snake game with pygame
# By @AbrahamChalave

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cubo(object):
    filas = 20
    w = 500
    def __init__(self, start, dirnx = 1, dirny = 0, color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, superf, eyes = False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(superf, self.color, (i * dis+1, j * dis+1, dis-2, dis-2))
        if eyes:
            cent = dis//2
            rad = 3
            circleMiddle = (i * dis + cent - rad, j * dis + 8)
            circleMiddle2 = (i * dis + dis - rad * 2, j * dis + 8)
            pygame.draw.circle(superf, (0, 0, 0), circleMiddle, rad)
            pygame.draw.circle(superf, (0, 0, 0), circleMiddle2, rad)

class snake(object):
    #A list for the blocks (cubo) in the body; a dictionary for the turns
    cuerpo = []
    vueltas = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cubo(pos)
        self.cuerpo.append(self.head)
        #Now the directions: dirnx and dirny are the directios in which the snake moves
        self.dirnx = 0
        slef.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_presses()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    slef.dirny = 0
                    self.vueltas[self.head.pos[:]] = [self.dirnx, self.dinry]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    slef.dirny = 0
                    self.vueltas[self.head.pos[:]] = [self.dirnx, self.dinry]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    slef.dirny = -1
                    self.vueltas[self.head.pos[:]] = [self.dirnx, self.dinry]
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    slef.dirny = 1
                    self.vueltas[self.head.pos[:]] = [self.dirnx, self.dinry]
                    #For every turn we save in a dictionary the position and the direction in which the snake turned

            #The next block iterates over the snake's body, moving each cube individually and removing the last one
            # in order to prevent the snake from increasing it's length
            for i, c in enumerate(self.cuerpo):
                p = c.pos[:]
                if p in self.vueltas:
                    vuelta = self.vueltas[p]
                    c.move(vuelta[0], vuelta[1])
                    if i == len(self.cuerpo) - 1:
                        self.vueltas.pop(p)
                else:
                    if c.dirnx == -1 and c.pos[0] <= 0:
                        c.pos = (c.rows - 1, c.pos[1])
                    elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                        c.pos = (c.pos[1], 0)
                    elif c.dirnx == 1 and c.pos[1] >= c.rows - 1:
                        c.pos = (c.pos[0], 0)
                    elif c.dirnx == -1 and c.pos[1] <= 0:
                        c.pos = (c.pos[1], c.rows - 1)
                    else:
                        c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = cubo(pos)
        self.body = []
        self.body.append(self.head)
        self.vueltas = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.cuerpo[-1]
        dx, dy = tail.dirnx, tail.dirny
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1]+1)))
        self.cuerpo[-1].dirnx = dx
        self.cuerpo[-1].dirny = dy

    def draw(self, superf):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(superf, True)
            else:
                c.draw(superf)


def drawGrid(w, filas, superf):
    espacio = w // filas # Int division to get the space between the grid lines
    x = 0
    y = 0
    for i in range(rows):
        x += espacio
        y += espacio
        pygame.draw.line(superf, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(superf, (255, 255, 255), (0, y), (w, y))
        # The las two tuples passed as arguments are the start position and the end position of the line

def redrawVentana(superf):
    global ancho, filas, s, snack
    superf.fill((0,0,0))
    s.draw(superf)
    snack.draw(superf)
    drawGrid(ancho, filas, superf)
    pygame.display.update()

def comida(filas, item):
    posiciones = item.body
    while True:
        x = random.randrange(filas)
        y = random.randrange(filas)
        if len(list(filter(lambda z:z.pos == (x,y), posiciones))) > 0:
            continue
        else:
            break
    return (x, y)

def message_box(tema, contenido):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebx.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():
    global ancho, filas, s, snack
    ancho = 500
    filas = 20
    win = pygame.display.set_mode((ancho, ancho))
    s = snake((255,0,0), (10,10))
    snack = cubo(comida(filas, s), color =(0, 255, 0))

    clock = pygame.time.Clock()
    flag = True

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.cuerpo[0].pos == snack.pos:
            s.addCube()
            snack = cubo(comida(filas, s), color =(0, 255, 0))

        for x in range(len(s.cuerpo)):
            if s.cuerpo[x].pos in list(map(lambda z:z.pos, s.cuerpo[x+1:])):
                print('Score: ', len(s.body))
                message_box('You Lost!', 'Play Again!')
                s.reset((10, 10)
                break

        redrawVentana(win)
