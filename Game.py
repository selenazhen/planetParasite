import pygame
from pygamegame import PygameGame
from Planet import Planet
import random
from Parasite import Parasite
import math
from gVariables import *

'''
Game.py
Actually implements the game
edit redraw all here
'''


class Game(PygameGame):
    def init(self):
        self.planetGroup = pygame.sprite.Group()
        self.parasite = pygame.sprite.Group()
        self.capturedPlanets = pygame.sprite.Group()
        
    def keyPressed(self, code, mod):
        pass
        
    def timerFired(self, dt):
        pass
    
    
    def redrawAll(self, screen):
        w,h,m = self.width,self.height,self.margin
        basicfont = pygame.font.Font("DINPro.otf", 20)
        textScore = basicfont.render('score: %d' % (self.score), True, WHITE)
        textScorerect = textScore.get_rect()
        textScorerect.centerx,textScorerect.centery = w//2, h-(m//2)
        textTitle = basicfont.render("planet parasite", True, WHITE)
        textTitlerect = textTitle.get_rect()
        textTitlerect.centerx,textTitlerect.centery = w//2, (m//2)
        
        #bounding box 
        # pygame.draw.rect(screen, WHITE,(self.borderX0, self.borderY0, 
        #                 self.width*3, self.height*3),2) 
        
        #initialize parasite 
        parasiteNew = Parasite() 
        self.parasite.add(parasiteNew)
            
        #add a planet every second or so
        if self.frameCount % 30 == 0: 
            planet = Planet()
            self.planetGroup.add(planet)
            print ('new planet')
        
        if event.type == pygame.KEYDOWN: 
            self.keyCont == True
        if event.type == pygame.KEYUP:
            self.keyCont == False
            
        for parasite in self.parasite:
            collisionList = pygame.sprite.spritecollide(parasite,self.planetGroup,  False, pygame.sprite.collide_circle)
            for captured in collisionList:
                self.planetGroup.remove(captured)
                self.score += 10
            
        self.planetGroup.draw(screen)
        self.parasite.draw(screen)
        
        pygame.draw.rect(screen, CHARCOAL,(0, 0, w, m)) #border top rect
        pygame.draw.rect(screen, CHARCOAL,(0, 0, m, h)) #border bottom rect
        pygame.draw.rect(screen, CHARCOAL,(w-m, 0, m, h)) #border top rect
        pygame.draw.rect(screen, CHARCOAL,(0, h-m, w, m)) #border top rect
        
        pygame.draw.rect(screen, WHITE,(m,m, w-(2*m),h-(2*m)), 2) #border
        screen.blit(textScore, textScorerect)
        screen.blit(textTitle, textTitlerect)

Game(600, 800).run()


# scrolling and gameplay by saturday night
# tentacles by monday 
# powerups by wednesday/deadline or focus on making tentacles more interesting

