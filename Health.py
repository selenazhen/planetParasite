'''
Health.py

implements the Health class
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import random
from gVariables import *


class Health(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        #randomize position with posX and posY
        posX = random.randrange(0,2*screenWidth)
        posY = random.randrange(0,2*screenHeight)
        #find location of image surface
        imageX = posX+planetSize*2
        imageY = posY+planetSize*2
        self.image = pygame.image.load('img/heart_filled_large.png').convert_alpha()
        self.coordsX = imageX//2 #keep circle centered on middle of image surface
        self.coordsY = imageY//2
        self.rect = self.image.get_rect()
        self.radius = planetSize
        # pygame.draw.circle(self.image, PINK, self.rect.center, self.radius)
        self.rect.centerx = posX
        self.rect.centery = posY
        
    def move(self, xMove,yMove):
        self.rect.centerx = self.rect.centerx + xMove
        self.rect.centery = self.rect.centery + yMove