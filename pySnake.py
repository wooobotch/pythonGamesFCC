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
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

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
