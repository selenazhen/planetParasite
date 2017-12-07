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


    def __init__(self,cx,cy):
        pygame.sprite.Sprite.__init__(self)
        #randomize position with posX and posY if specific location is not given
        if cx == 0 and cy == 0: 
            posX = random.randrange(250,2*screenWidth)
            posY = random.randrange(250,2*screenHeight)
        else: 
            posX = cx
            posY = cy
        # posX = random.randrange(0,2*screenWidth)
        # posY = random.randrange(0,2*screenHeight)
        #find location of image surface
        self.imageX = posX+planetSize*4
        self.imageY = posY+planetSize*4
        self.image = pygame.Surface((self.imageX,self.imageY),pygame.SRCALPHA) #self.imageX and self.imageY = width and height
        # keep circle centered on middle of image surface, regardless of image surface size
        self.coordsX = self.imageX//2
        self.coordsY = self.imageY//2
        self.color = WHITE
        self.rect = self.image.get_rect()
        self.inhabitedSize = planetSize
        self.radius = self.inhabitedSize
        # self.radius = .5*parasiteSize*2
        
        # pygame.draw.circle(self.image, self.color,(self.coordsX,self.coordsY),
        #                     self.inhabitedSize)
        self.divisions = 100
        self.length = 0
        
    def move(self, xMove,yMove):
        self.rect.centerx = self.rect.centerx + xMove
        self.rect.centery = self.rect.centery + yMove
    
    def dotted(self):
        self.radius = self.inhabitedSize*2
        for div in range(self.divisions):
            # self.length = random.randrange(25,40)
            divAngle = div*((math.pi*2)/self.divisions)
            outerDivX = self.coordsX + ((self.radius) * math.cos(divAngle))
            outerDivY = self.coordsY + ((self.radius) * math.sin(divAngle))
            innerDivX = self.coordsX + ((self.radius) * math.cos(divAngle))
            innerDivY = self.coordsY + ((self.radius) * math.sin(divAngle))
            pygame.draw.line(self.image,self.color,(innerDivX,innerDivY), (outerDivX, outerDivY), 1)
    
    def stopUpdating(self,newColor):
        # self.inhabitedSize = int(.5*parasiteSize)
        #draw filled circle over previous circle
        pygame.draw.circle(self.image, newColor,(self.coordsX,self.coordsY),
                            self.inhabitedSize+5)
        
    def update(self):
        self.inhabitedSize += 1
        pygame.draw.circle(self.image, CHARCOAL,(self.coordsX,self.coordsY),
                            self.inhabitedSize+5)
        pygame.draw.circle(self.image, self.color,(self.coordsX,self.coordsY),
                            self.inhabitedSize, 4)
                            
        
