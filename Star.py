'''
Star.py

implements the Star class
'''
import pygame
import random
from gVariables import *

class Star(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #randomize position with posX and posY
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
        pygame.draw.circle(self.image, self.color,(self.coordsX,self.coordsY),
                            self.radius)
        
    def move(self, xMove,yMove):
        self.rect.centerx = self.rect.centerx + xMove
        self.rect.centery = self.rect.centery + yMove