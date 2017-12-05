'''
Star.py

implements the Star class
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import random
from gVariables import *


class Star(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        posX = random.randrange(0,screenWidth*2)
        posY = random.randrange(0,screenHeight*2)
        #find location of image surface
        imageX = posX+planetSize*2
        imageY = posY+planetSize*2
        self.image = pygame.Surface((imageX,imageY),pygame.SRCALPHA)
        self.coordsX = imageX//2 #keep circle centered on middle of image surface
        self.coordsY = imageY//2
        self.rect = self.image.get_rect()
        self.radius = 2
        self.color = DARKGREY
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        pygame.draw.circle(self.image, self.color,(self.coordsX,self.coordsY),
                            self.radius)
        # self.image = pygame.image.load('img/planet1.png').convert_alpha()
        
    def move(self, xMove,yMove):
        self.rect.centerx = self.rect.centerx + xMove
        self.rect.centery = self.rect.centery + yMove