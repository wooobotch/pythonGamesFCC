# 2020 Quarantine python project
# A simple terminal snake game with pygame
# By @AbrahamChalave

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cubo(object):
    filas = 0
    w = 0
    def __init__(self, sart, dirnx = 1, dirny = 0, color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, superf, eyes = False):
        pass


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
            for i, c in enumerate(self.cuerpo)
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
        pass

    def addCube(self):
        pass

    def draw(self, superf):
        pass


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
    global ancho, filas
    superf.fill((0,0,0))
    drawGrid(ancho, filas, superf)
    pygame.display.update()

def comida(filas, items):
    pass

def message_box(tema, contenido):
    pass

def main():
    global ancho, filas
    ancho = 500
    filas = 20
    win = pygame.display.set_mode((ancho, ancho))
    bicho = snake((255,0,0), (10,10))
    clock = pygame.time.Clock()
    flag = True

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redraVentana(win)

# 00:55:20
