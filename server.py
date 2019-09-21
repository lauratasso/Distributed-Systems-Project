import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pong Pong!")

#Creating a ball and background.
back = pygame.Surface((640,480))
background = back.convert()
background.fill((0,0,0))


#clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        
    
    screen.blit(background,(0,0))
    frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
    middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
    
    pygame.display.update()

