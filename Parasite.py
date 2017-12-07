'''
Parasite.py

implements the Parasite class
'''
import pygame
import random
import math
from gVariables import *

class Parasite(pygame.sprite.Sprite):

    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((screenWidth,screenHeight),pygame.SRCALPHA)
        self.coordsX = screenWidth//2
        self.coordsY = screenHeight//2
        self.size = size
        self.radius = size
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, WHITE,(screenWidth//2,screenHeight//2),
                            size, 5)
        
    def update(self, tentacleRadius):
        self.radius = self.size + tentacleRadius
        
    def move(self, xMove,yMove):
        self.rect.centerx = self.rect.centerx + xMove
        self.rect.centery = self.rect.centery + yMove