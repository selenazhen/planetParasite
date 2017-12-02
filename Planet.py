'''
Planet.py

implements the Planet class
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import random
from GameObject import GameObject

screenWidth = 600
screenHeight = 800
planetSize = screenWidth//30
CHARCOAL = (28,28,28)
WHITE = (255,255,255)
BLACK = (0,0,0)

class Planet(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.coordsX = random.randrange(0,screenWidth)
        self.coordsY = random.randrange(0,screenHeight)
        self.image = pygame.Surface((self.coordsX+(1.5*planetSize), self.coordsY + (1.5*planetSize)), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE,(self.coordsX,self.coordsY),
                            planetSize, 2) #testing circle
        
        
        # self.image = pygame.image.load('img/planet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.coordsX
        self.rect.centery = self.coordsY
    def move(self, xMove,yMove):
        self.rect.centerx = self.rect.centerx + xMove
        self.rect.centery = self.rect.centery + yMove