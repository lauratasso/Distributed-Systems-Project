import pygame
from pygame.locals import *

class Ball:

    # class constructor
    def __init__(self, rgb, pos_x, pos_y):
        self.sur = pygame.Surface((16, 16))
        self.circ = pygame.draw.circle(self.sur, rgb, (8, 8), 8)
        self.circle = self.sur.convert()
        self.circle.set_colorkey((0, 0, 0))

        self.circle_x, self.circle_y = pos_x, pos_y
        self.speed_x, self.speed_y, self.speed_circ = 250., 250., 250.

    def move(self, screen, clock):
        screen.blit(self.circle, (self.circle_x, self.circle_y))

        time_passed = clock.tick(30)
        time_sec = time_passed / 1000.0

        self.circle_x += self.speed_x * time_sec
        self.circle_y += self.speed_y * time_sec

        if self.circle_x <= 10.:
            if self.circle_y >= 7.5 and self.circle_y <= 470:
                self.circle_x = 20.
                self.speed_x = -self.speed_x
        if self.circle_x >= 630.:
            if self.circle_y >= 7.5 and self.circle_y <= 470:
                self.circle_x = 605.
                self.speed_x = -self.speed_x
        if self.circle_y <= 10.:
            self.speed_y = -self.speed_y
            self.circle_y = 10.
        elif self.circle_y >= 457.5:
            self.speed_y = -self.speed_y
            self.circle_y = 457.5
