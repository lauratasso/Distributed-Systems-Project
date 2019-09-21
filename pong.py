import pygame
from pygame.locals import *
from sys import exit
import random

#import class from classes folder
from classes.ball import Ball

pygame.init()

screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pong Pong!")

#Creating a ball and background.
back = pygame.Surface((640,480))
background = back.convert()
background.fill((0,0,0))
ball_list = []

# Create and add Ball instance to ball_list
# To create a ball, it its necessary to inform the rgb triple and the ball initial coordinates
ball_list.append(Ball((0, 0, 255), 155, 155))
ball_list.append(Ball((184, 181, 245), 3, 3))

#clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    screen.blit(background,(0,0))
    frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
    middle_line = pygame.draw.aaline(screen,(255,255,255),(320,5),(320,475))
    
    # movement of each ball
    for ball in ball_list:
        ball.move(screen, clock)

    pygame.display.update()
