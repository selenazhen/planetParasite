'''
Parasite.py

implements the Parasite class
'''
import pygame
import random
from gVariables import *


class Parasite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((screenWidth,screenHeight),pygame.SRCALPHA)
        self.coordsX = screenWidth//2
        self.coordsY = screenHeight//2
        self.radius = screenWidth//8
        self.rect = self.image.get_rect()    
        # pygame.draw.circle(self.image, PINK, self.rect.center, self.radius)
        pygame.draw.circle(self.image, WHITE,(screenWidth//2,screenHeight//2),
                            parasiteSize, 5)
        