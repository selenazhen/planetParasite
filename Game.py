import pygame
import random
import math
from pygamegame import PygameGame
from Planet import Planet
from Parasite import Parasite
from Tentacles import Tentacles
from Inhabited import Inhabited
from Star import Star

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
        self.tentacles = pygame.sprite.Group()
        
        tentaclesNew = Tentacles()
        self.tentacles.add(tentaclesNew)
        
        self.inhabitedGroup = pygame.sprite.Group()
        
        self.starGroup = pygame.sprite.Group()
        
        #add static stars
        for point in range(100):
            starNew = Star()
            self.starGroup.add(starNew)
            
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
        
        #add uninhabited planets
        if self.frameCount % 50 == 0:
            inhabitedNew = Inhabited()
            self.inhabitedGroup.add(inhabitedNew)
            print ('new uninhabited')
        
        
        #bounding box 
        # pygame.draw.rect(screen, WHITE,(self.borderX0, self.borderY0, 
        #                 self.width*3, self.height*3),2) 
        
        #add a planet every second or so
        if self.frameCount % 15 == 0: 
            planet = Planet()
            self.planetGroup.add(planet)
            print ('new planet')
            
        for parasite in self.parasite:
            collisionList = pygame.sprite.spritecollide(parasite,self.planetGroup,  False, 
                            pygame.sprite.collide_circle)
            for captured in collisionList:
                self.planetGroup.remove(captured)
                self.score += 10
        
        parasiteNew = Parasite() 
        self.parasite.add(parasiteNew)
        
        # tentaclesNew = Tentacles()
        # self.tentacles.add(tentaclesNew)
        
        if self.frameCount % 10 == 0: #inhabited planets get larger and larger as time goes on
            for inhabited in self.inhabitedGroup:
                #if inhabited planet gets larger than a certain size
                if (inhabited.inhabitedSize >= .2*min(inhabited.imageX,inhabited.imageY)) or(
                    inhabited.inhabitedSize >= .5*parasiteSize):
                    # print ('its too big')
                    inhabited.stopUpdating()
                    inhabited.dotted()
                    inhabited.color = RED
                else:
                    inhabited.update()
        
        
        self.starGroup.draw(screen)
        self.planetGroup.draw(screen)
        self.inhabitedGroup.draw(screen)
        self.parasite.draw(screen)
        self.tentacles.draw(screen)
        pygame.draw.rect(screen, CHARCOAL,(0, 0, w, m)) #border top rect
        pygame.draw.rect(screen, CHARCOAL,(0, 0, m, h)) #border bottom rect
        pygame.draw.rect(screen, CHARCOAL,(w-m, 0, m, h)) #border top rect
        pygame.draw.rect(screen, CHARCOAL,(0, h-m, w, m)) #border top rect
        
        pygame.draw.rect(screen, WHITE,(m,m, w-(2*m),h-(2*m)), 2) #border
        screen.blit(textScore, textScorerect)
        screen.blit(textTitle, textTitlerect)
        

Game(screenWidth, screenHeight).run()



