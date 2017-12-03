'''
Parasite.py

implements the Parasite class
'''
import pygame
import random
import math
from gVariables import *


class Parasite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((screenWidth,screenHeight),pygame.SRCALPHA)
        self.coordsX = screenWidth//2
        self.coordsY = screenHeight//2
        # self.radius = parasiteSize - 2
        # self.rect = self.image.get_rect()    
        # pygame.draw.circle(self.image, PINK, self.rect.center, self.radius)
        # pygame.draw.circle(self.image, WHITE,(screenWidth//2,screenHeight//2),
                            parasiteSize, 5)
        self.divisions = 100
        for div in range(self.divisions):
            divAngle = div*((math.pi*2)/self.divisions)
            length = random.randrange(20,40)
            outerDivX = self.coordsX + ((parasiteSize+length) * math.cos(divAngle))
            outerDivY = self.coordsY + ((parasiteSize+length) * math.sin(divAngle))
            innerDivX = self.coordsX + ((parasiteSize+6) * math.cos(divAngle))
            innerDivY = self.coordsY + ((parasiteSize+6) * math.sin(divAngle))
            pygame.draw.line(self.image,WHITE,(innerDivX,innerDivY), (outerDivX, outerDivY), 1)
            # pygame.draw.line(self.image,PINK,(self.coordsX,self.coordsY), (outerDivX, outerDivY), 1)
            # pygame.draw.line(self.image,WHITE,(self.coordsX,self.coordsY), (innerDivX, innerDivY), 1)
    