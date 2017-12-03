'''
Planet.py

implements the Planet class
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import random
from gVariables import *


class Planet(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        #randomize position with posX and posY
        posX = random.randrange(planetSize,screenWidth-planetSize)
        posY = random.randrange(planetSize,screenHeight-planetSize)
        #find location of image surface
        imageX = posX+planetSize*2
        imageY = posY+planetSize*2
        self.image = pygame.Surface((imageX,imageY),pygame.SRCALPHA)
        self.coordsX = imageX//2 #keep circle centered on middle of image surface
        self.coordsY = imageY//2
        self.rect = self.image.get_rect()
        self.radius = planetSize-2
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        pygame.draw.circle(self.image, WHITE,(self.coordsX,self.coordsY),
                            planetSize, 2) #testing circle
        # self.image = pygame.image.load('img/planet1.png').convert_alpha()
        
    def move(self, xMove,yMove):
        self.rect.centerx = self.rect.centerx + xMove
        self.rect.centery = self.rect.centery + yMove