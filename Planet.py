'''
Planet.py

implements the Planet class
'''
import pygame
import random
from gVariables import *

class Planet(pygame.sprite.Sprite):

    def __init__(self,width,color):
        pygame.sprite.Sprite.__init__(self)
        #randomize position with posX and posY
        posX = random.randrange(0,2*screenWidth)
        posY = random.randrange(0,2*screenHeight)
        #find location of image surface
        imageX = posX+planetSize*2
        imageY = posY+planetSize*2
        self.image = pygame.Surface((imageX,imageY),pygame.SRCALPHA)
        self.coordsX = imageX//2 #keep circle centered on middle of image surface
        self.coordsY = imageY//2
        self.rect = self.image.get_rect()
        self.radius = planetSize-2
        self.color = color
        pygame.draw.circle(self.image, CHARCOAL,(self.coordsX,self.coordsY),
                            planetSize+5) #testing circle
        pygame.draw.circle(self.image, self.color,(self.coordsX,self.coordsY),
                            planetSize, width) #testing circle
        
    def move(self, xMove,yMove):
        self.rect.centerx = self.rect.centerx + xMove
        self.rect.centery = self.rect.centery + yMove