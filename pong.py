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
circ_sur = pygame.Surface((16,16))
circ = pygame.draw.circle(circ_sur,(0,255,0),(8,8),8)
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))

# some definitions
circle_x, circle_y = 307.5, 232.5
speed_x, speed_y, speed_circ = 250., 250., 250.
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
    screen.blit(circle,(circle_x,circle_y))
    
# movement of circle
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0
    
    circle_x += speed_x * time_sec
    circle_y += speed_y * time_sec
    ai_speed = speed_circ * time_sec

    if circle_x <= 10.:
        if circle_y >= 7.5 and circle_y <= 470:
            circle_x = 20.
            speed_x = -speed_x
    if circle_x >= 630.:
        if circle_y >= 7.5 and circle_y <= 470:
            circle_x = 605.
            speed_x = -speed_x
    if circle_y <= 10.:
        speed_y = -speed_y
        circle_y = 10.
    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5

    pygame.display.update()
