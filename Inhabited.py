'''
Inhabited.py

implements the Inhabited class
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import random
import math
from gVariables import *


class Inhabited(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        #randomize position with posX and posY
        posX = random.randrange(300,2*screenWidth)
        posY = random.randrange(300,2*screenHeight)
        # posX = random.randrange(0,2*screenWidth)
        # posY = random.randrange(0,2*screenHeight)
        #find location of image surface
        self.imageX = posX+planetSize*2
        self.imageY = posY+planetSize*2
        self.image = pygame.Surface((self.imageX,self.imageY),pygame.SRCALPHA) #self.imageX and self.imageY = width and height
        self.coordsX = self.imageX//2 #keep circle centered on middle of image surface, regardless of image surface size
        self.color = WHITE
        self.coordsY = self.imageY//2
        self.rect = self.image.get_rect()
        self.radius = .5*parasiteSize*2
        self.inhabitedSize = planetSize
        
        # pygame.draw.circle(self.image, self.color,(self.coordsX,self.coordsY),
        #                     self.inhabitedSize)
        self.divisions = 100
        self.length = 0
        
    def move(self, xMove,yMove):
        self.rect.centerx = self.rect.centerx + xMove
        self.rect.centery = self.rect.centery + yMove
    
    def dotted(self):
        if self.radius > self.imageX:
            self.radius = self.imageX//2
        if self.radius > self.imageY:
            self.radius = self.imageY//2
        for div in range(self.divisions):
            # self.length = random.randrange(25,40)
            divAngle = div*((math.pi*2)/self.divisions)
            outerDivX = self.coordsX + ((self.radius) * math.cos(divAngle))
            outerDivY = self.coordsY + ((self.radius) * math.sin(divAngle))
            innerDivX = self.coordsX + ((self.radius) * math.cos(divAngle))
            innerDivY = self.coordsY + ((self.radius) * math.sin(divAngle))
            pygame.draw.line(self.image,self.color,(innerDivX,innerDivY), (outerDivX, outerDivY), 1)
    
    def stopUpdating(self):
        self.inhabitedSize = int(.5*parasiteSize)
        self.inhabitedSize += 1
        pygame.draw.circle(self.image, self.color,(self.coordsX,self.coordsY),
                            self.inhabitedSize)
        
    def update(self):
        self.inhabitedSize += 1
        pygame.draw.circle(self.image, CHARCOAL,(self.coordsX,self.coordsY),
                            self.inhabitedSize+5)
        pygame.draw.circle(self.image, self.color,(self.coordsX,self.coordsY),
                            self.inhabitedSize, 4)
                            
        
