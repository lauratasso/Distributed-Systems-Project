import pygame
from pygame.locals import *
from sys import exit
import random

# import class from classes folder
from ball import Ball


class Tela:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 480), 0, 32)
        pygame.display.set_caption("Pong Pong!")

        # Creating a ball and background.
        back = pygame.Surface((640, 480))
        self.background = back.convert()
        self.background.fill((0, 0, 0))
        self.ball_list = []

        # clock and font objects
        self.clock = pygame.time.Clock()
        font = pygame.font.SysFont("calibri", 40)

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            self.screen.blit(self.background, (0, 0))
            frame = pygame.draw.rect(
                self.screen, (255, 255, 255), Rect((5, 5), (630, 470)), 2)
            middle_line = pygame.draw.aaline(
                self.screen, (255, 255, 255), (320, 5), (320, 475))

            # movement of each ball
            for ball in self.ball_list:
                self.screen.blit(ball.circle, (ball.circle_x, ball.circle_y))

            pygame.display.update()

    def update(self):
        pygame.display.update()
