from LightParticle import LightParticle
from globals import SCREEN_X, SCREEN_Y
import pygame
import random

pygame.init()


screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("lightspeed")

#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed
particles = []
ticker = 0

while not doExit:
    ticker += 1
    screen.fill((0,0,0))
    if ticker < 500:
        particles.append(LightParticle())
    
    for particle in particles:
        particle.move()

        
        particle.draw(screen)

    pygame.display.flip()