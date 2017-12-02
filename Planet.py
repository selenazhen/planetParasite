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
planetSize = screenWidth//20
CHARCOAL = (28,28,28)
WHITE = (255,255,255)
BLACK = (0,0,0)

class Planet(pygame.sprite.Sprite):

    def __init__(self, xPosition, yPosition):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/planet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = xPosition
        self.rect.centery = yPosition
    def move(self, xMove,yMove):
        self.rect.centerx = self.rect.centerx + xMove
        self.rect.centery = self.rect.centery + yMove