'''
Instructions.py

implements the Instructions class
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import random
from gVariables import *


class Instructions(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((screenWidth,screenHeight),pygame.SRCALPHA)
        self.coordsX = screenWidth//2
        self.coordsY = screenHeight//2
        self.rect = self.image.get_rect()
        
        #instructions title
        titleFont = pygame.font.Font("DINPro.otf", 30)
        titleText = titleFont.render('how to play', True, WHITE)
        self.titleRect = titleText.get_rect()
        self.titleRect.centerx = screenWidth//2
        self.titleRect.centery = screenHeight//8
        
        self.image.blit(titleText, self.titleRect)
        
        
    def move(self, xMove,yMove):
        self.rect.centerx = self.rect.centerx + xMove
        self.rect.centery = self.rect.centery + yMove