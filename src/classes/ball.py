import pygame
from pygame.locals import *


class Ball:

    # Construtor da classe. Recebe coordenadas e cores da bola
    def __init__(self, rgb, pos_x, pos_y):
        self.sur = pygame.Surface((16, 16))
        self.circ = pygame.draw.circle(self.sur, rgb, (8, 8), 8)
        self.circle = self.sur.convert()
        self.circle.set_colorkey((0, 0, 0))

        self.circle_x, self.circle_y = pos_x, pos_y
        self.speed_x, self.speed_y, self.speed_circ = 250., 250., 250.
