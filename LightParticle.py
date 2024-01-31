import math
import random
import pygame
from globals import SCREEN_X, SCREEN_Y, CENTER, MAX_SIZE

class LightParticle:
    def __init__(self):
        self.reset()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.xpos, self.ypos), self.size)

    def move(self):
        self.size = (pygame.Vector2(self.xpos, self.ypos).distance_to(CENTER)/CENTER[0])*MAX_SIZE
        if self.size < 1:
            self.size = 1

        self.color = self.color.move_towards(self.endColor, self.weight)
        self.weight *= (random.randrange(1001,1025)/1000)
        self.xpos, self.ypos = pygame.Vector2(self.xpos, self.ypos).move_towards(self.goTo, self.weight)
        if not (self.xpos > 0 and self.xpos < SCREEN_X and self.ypos > 0 and self.ypos < SCREEN_Y):
            self.reset()

    def reset(self):
        #TYPES OF COLORS POSSIBLE: vignette, normal, combo, RB, pastel, fullrand
        self.color, self.endColor = self.setColors("pastel")
        self.size = 2
        self.weight = 0.1
        self.xpos, self.ypos = CENTER
        self.angle = (random.randint(0,360)*(math.pi/180))
        self.goTo = pygame.Vector2(SCREEN_X/2 + (math.cos(self.angle) * SCREEN_X), SCREEN_Y/2 + (math.sin(self.angle) * SCREEN_Y))

    def setColors(self, colorWay):
        if colorWay == "combo":
            coinFlip = random.randint(0,1)
            color = pygame.Vector3(255,255,255) if coinFlip == 0 else pygame.Vector3(0,0,0)
            endColor = pygame.Vector3(0,0,0) if coinFlip == 0 else pygame.Vector3(255,255,255)
        elif colorWay == "normal":
            color = pygame.Vector3(0, 0, 0)
            endColor = pygame.Vector3(255, 255, 255)
        elif colorWay == "vignette":
            color = pygame.Vector3(255, 255, 255)
            endColor = pygame.Vector3(0, 0, 0)
        elif colorWay == "RB":
            color = pygame.Vector3(random.randint(155, 255), random.randint(0, 50), 0)
            endColor = pygame.Vector3(0, random.randrange(50, 255), random.randrange(100, 200))
        elif colorWay == "pastel":
            color = pygame.Vector3(220, 220, 220)
            endColor = pygame.Vector3(random.randrange(100, 255), random.randrange(100, 255), random.randrange(100, 255))
        elif colorWay == "fullrand":
            color = pygame.Vector3(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            endColor = pygame.Vector3(random.randint(0, 155), random.randint(0, 155), random.randint(0, 155))
        return (color, endColor)