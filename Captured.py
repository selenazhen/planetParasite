
'''
Parasite.py

implements the Parasite class
'''
import pygame
import random
import math
from gVariables import *



class Captured(pygame.sprite.Sprite):
    def __init__(self,cx,cy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((screenWidth,screenHeight),pygame.SRCALPHA)
        self.coordsX = cx #keep circle centered on middle of image surface
        self.coordsY = cy
        self.rect = self.image.get_rect()
        self.radius = planetSize
        self.speed = -2
    
    def getSpeed(self):
        return random.randrange(3, 10)
        
    def update(self):  
        pygame.draw.circle(self.image, PINK,(self.coordsX,self.coordsY),
                            planetSize, 2)