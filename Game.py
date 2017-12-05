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
        self.tentacleGroup = pygame.sprite.Group()
        
        # tentacleGroupNew = Tentacles()
        # self.tentacleGroup.add(tentacleGroupNew)
        
        self.inhabitedGroup = pygame.sprite.Group()
        self.formedInhabitedGroup = pygame.sprite.Group()
        
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
        self.screen.fill(self.bgColor)
        w,h,m = self.width,self.height,self.margin
        basicfont = pygame.font.Font("DINPro.otf", 20)
        textScore = basicfont.render('score: %d   lives: %d' % (self.score,self.lives), True, WHITE)
        textScorerect = textScore.get_rect()
        textScorerect.centerx,textScorerect.centery = w//2, h-(m//2)
        textTitle = basicfont.render("planet parasite", True, WHITE)
        textTitlerect = textTitle.get_rect()
        textTitlerect.centerx,textTitlerect.centery = w//2, (m//2)
        
        #add uninhabited planets
        if self.frameCount % 30 == 0:
            inhabitedNew = Inhabited()
            self.inhabitedGroup.add(inhabitedNew)
            print ('new uninhabited')
        
        #bounding box 
        # pygame.draw.rect(screen, WHITE,(self.borderX0, self.borderY0, 
        #                 self.width*3, self.height*3),2) 
        
        #add a planet every so often
        if self.frameCount % 7 == 0: 
            planet = Planet()
            self.planetGroup.add(planet)
            print ('new planet')
            
        for parasite in self.parasite:
            collisionPlanetsList = pygame.sprite.spritecollide(parasite,self.planetGroup,  False, 
                            pygame.sprite.collide_circle)
            for capturedPlanet in collisionPlanetsList:
                self.planetGroup.remove(capturedPlanet)
                self.score += 10
            collisionInhabitedList = pygame.sprite.spritecollide(parasite,self.formedInhabitedGroup,  False, 
                            pygame.sprite.collide_circle)
            for hitInhabited in collisionInhabitedList:
                hitInhabited.stopUpdating(PINK) #turn the hit inhabited planet pink for right now 
                # self.formedInhabitedGroup.remove(hitInhabited) #remove inhabited if you want to
                self.lives -= 1
        
        # for tentacle in self.tentacleGroup:
        #     collisionTentaclesList = pygame.sprite.spritecollide(tentacle,self.planetGroup,  False, 
        #                     pygame.sprite.collide_circle)
        #     for capturedPlanet in collisionTentaclesList:
        #         self.planetGroup.remove(capturedPlanet)
        #         self.score += 10
        #         
        #     collisionInhabitedList = pygame.sprite.spritecollide(tentacle,self.formedInhabitedGroup,  False, 
        #                     pygame.sprite.collide_circle)
        #     for hitInhabited in collisionInhabitedList:
        #         self.tentacleGroup.remove(tentacle)
        #         hitInhabited.stopUpdating(PINK) #turn the hit inhabited planet pink for right now 
        #         # self.formedInhabitedGroup.remove(hitInhabited) #remove inhabited if you want to
        #         self.lives -= 1
        
        parasiteNew = Parasite() 
        self.parasite.add(parasiteNew)
        
        self.divisions = 100
        for div in range(self.divisions):
            divAngle = div*((math.pi*2)/self.divisions)
            self.length = random.randrange(25,40)
            outerDivX = self.width//2 + ((parasiteSize+self.length) * math.cos(divAngle))
            outerDivY = self.height//2 + ((parasiteSize+self.length) * math.sin(divAngle))
            innerDivX = self.width//2 + ((parasiteSize+6) * math.cos(divAngle))
            innerDivY = self.height//2 + ((parasiteSize+6) * math.sin(divAngle))
            tentacleNew = pygame.draw.line(self.screen,WHITE,(innerDivX,innerDivY), (outerDivX, outerDivY), 1)
            # self.tentacleGroup.add(tentacleNew)
        
        # tentacleGroupNew = Tentacles()
        # self.tentacleGroup.add(tentacleGroupNew)
        
        # if self.frameCount % 1 == 0: #inhabited planets get larger and larger as time goes on
        for inhabited in self.inhabitedGroup:
            #if inhabited planet gets larger than a certain size
            if (inhabited.inhabitedSize >= .15*min(inhabited.imageX,inhabited.imageY)):
                # print ('its too big')
                inhabited.stopUpdating(WHITE)
                inhabited.dotted()
                self.formedInhabitedGroup.add(inhabited)
                self.inhabitedGroup.remove(inhabited)
            else:
                inhabited.update()
        
        self.starGroup.draw(screen)
        self.planetGroup.draw(screen)
        self.inhabitedGroup.draw(screen)
        self.formedInhabitedGroup.draw(screen)
        self.parasite.draw(screen)
        self.tentacleGroup.draw(screen)
        
        pygame.draw.rect(screen, CHARCOAL,(0, 0, w, m)) #border top rect
        pygame.draw.rect(screen, CHARCOAL,(0, 0, m, h)) #border bottom rect
        pygame.draw.rect(screen, CHARCOAL,(w-m, 0, m, h)) #border top rect
        pygame.draw.rect(screen, CHARCOAL,(0, h-m, w, m)) #border top rect
        
        pygame.draw.rect(screen, WHITE,(m,m, w-(2*m),h-(2*m)), 2) #border
        screen.blit(textScore, textScorerect)
        screen.blit(textTitle, textTitlerect)
        

Game(screenWidth, screenHeight).run()



