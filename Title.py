'''
Title.py

implements the Title class
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import random
from gVariables import *

class Title(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((screenWidth,screenHeight),pygame.SRCALPHA)
        self.coordsX = screenWidth//2
        self.coordsY = screenHeight//2
        # self.radius = parasiteSize
        self.rect = self.image.get_rect()  
        
        
        #planet parasite title
        titleFont = pygame.font.Font("DINPro.otf", 50)
        titleText = titleFont.render('planet parasite', True, WHITE)
        self.titleRect = titleText.get_rect()
        self.titleRect.centerx = screenWidth//2
        self.titleRect.centery = screenHeight//4
        
        # press space to play
        playFont = pygame.font.Font("DINPro.otf", 25)
        playText = playFont.render("press 'space' to play", True, WHITE)
        self.playRect = playText.get_rect()
        self.playRect.centerx = screenWidth//2
        self.playRect.centery = 3*(screenHeight//4)
        
        # press h for instructions
        instructFont = pygame.font.Font("DINPro.otf", 25)
        instructText = instructFont.render("press 'h' for instructions", True, WHITE)
        self.instructRect = instructText.get_rect()
        self.instructRect.centerx = screenWidth//2
        self.instructRect.centery = 3*(screenHeight//4) + 40
        
        # press escape at any time to quit the game
        quitFont = pygame.font.Font("DINPro.otf", 25)
        quitText = quitFont.render("press 'escape' during gameplay to quit", True, WHITE)
        self.quitRect = quitText.get_rect()
        self.quitRect.centerx = screenWidth//2
        self.quitRect.centery = 3*(screenHeight//4) + 80
        
        self.image.blit(titleText, self.titleRect)
        self.image.blit(playText, self.playRect)
        self.image.blit(instructText, self.instructRect)
        self.image.blit(quitText, self.quitRect)
        
    def move(self, xMove,yMove):
        self.rect.centerx = self.rect.centerx + xMove
        self.rect.centery = self.rect.centery + yMove