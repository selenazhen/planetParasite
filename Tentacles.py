'''
Tentacles.py

implements the v class
'''
import pygame
import random
import math
from gVariables import *



# class Tentacles(pygame.sprite.Sprite):
# 
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((screenWidth,screenHeight),pygame.SRCALPHA)
#         self.coordsX = screenWidth//2
#         self.coordsY = screenHeight//2
#         self.radius = parasiteSize + 40
#         self.rect = self.image.get_rect()    
#         # pygame.draw.circle(self.image, PINK, self.rect.center, self.radius)
#         # pygame.draw.circle(self.image, WHITE,(screenWidth//2,screenHeight//2),
#                             # parasiteSize, 5)
#         self.divisions = 100
#         # self.length = 30
#         for div in range(self.divisions):
#             divAngle = div*((math.pi*2)/self.divisions)
#             self.length = random.randrange(25,40)
#             outerDivX = self.coordsX + ((parasiteSize+self.length) * math.cos(divAngle))
#             outerDivY = self.coordsY + ((parasiteSize+self.length) * math.sin(divAngle))
#             innerDivX = self.coordsX + ((parasiteSize+6) * math.cos(divAngle))
#             innerDivY = self.coordsY + ((parasiteSize+6) * math.sin(divAngle))
#             pygame.draw.line(self.image,WHITE,(innerDivX,innerDivY), (outerDivX, outerDivY), 1)
#             # pygame.draw.line(self.image,PINK,(self.coordsX,self.coordsY), (outerDivX, outerDivY), 1)
#             # pygame.draw.line(self.image,WHITE,(self.coordsX,self.coordsY), (innerDivX, innerDivY), 1)
#     
#     # def move(self,length):
#     #     print ('its moving')
#     #     self.divisions = 36
#         # self.coordsX += self.coordsX + length
#         # self.image = pygame.Surface((screenWidth,screenHeight),pygame.SRCALPHA


class Tentacle(pygame.sprite.Sprite):

    def __init__(self,innerDivX,innerDivY,outerDivX,outerDivY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((screenWidth,screenHeight),pygame.SRCALPHA)
        self.coordsX = screenWidth//2
        self.coordsY = screenHeight//2
        self.radius = parasiteSize + 40
        self.rect = self.image.get_rect() 
        pygame.draw.line(self.image,WHITE,(innerDivX,innerDivY), (outerDivX, outerDivY), 1)
    
    # def move(self,length):
    #     print ('its moving')
    #     self.divisions = 36
        # self.coordsX += self.coordsX + length
        # self.image = pygame.Surface((screenWidth,screenHeight),pygame.SRCALPHA)
        