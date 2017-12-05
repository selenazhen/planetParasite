
'''
Dotted.py

implements the Dotted class
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import random
import math
from gVariables import *


class Dotted(pygame.sprite.Sprite):


    def __init__(self,lenInner):
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
        self.radius = planetSize-5
        # pygame.draw.circle(self.image, ORANGE, self.rect.center, self.radius)
        # pygame.draw.circle(self.image, WHITE,(self.coordsX,self.coordsY),
                            # planetSize, 2) #testing circle
        pygame.draw.circle(self.image, WHITE,(self.coordsX,self.coordsY),
                            planetSize)
        # pygame.draw.circle(self.image, WHITE,(self.coordsX,self.coordsY),
        #                     planetSize*3,1)
        self.divisions = 100
        self.lenInner = 10
        self.lenOutter = 30
        self.dir = 'out'
    
    
    def update(self,x):
        self.lenOutter = self.lenOutter + x #expand
        if self.lenOutter > 50: self.dir = 'in'
        for div in range(self.divisions):
            divAngle = div*((math.pi*2)/self.divisions)
            outerDivX = self.coordsX + ((self.lenOutter) * math.cos(divAngle))
            outerDivY = self.coordsY + ((self.lenOutter) * math.sin(divAngle))
            innerDivX = self.coordsX + ((self.lenOutter) * math.cos(divAngle))
            innerDivY = self.coordsY + ((self.lenOutter) * math.sin(divAngle))
            pygame.draw.line(self.image,WHITE,(innerDivX,innerDivY), (outerDivX, outerDivY), 1)
        
        print ('expanding')