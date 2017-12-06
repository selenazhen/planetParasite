import pygame
import random
import math
from pygamegame import PygameGame
from Planet import Planet
from Parasite import Parasite
from Inhabited import Inhabited
from Star import Star
from Captured import Captured
from Title import Title
from Instructions import Instructions
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
        self.inhabitedGroup = pygame.sprite.Group()
        self.formedInhabitedGroup = pygame.sprite.Group()
        self.capturedGroup = pygame.sprite.Group()
        
        self.titleGroup = pygame.sprite.Group()
        self.parasiteTitle = pygame.sprite.Group()
        # self.tentacleGroup = pygame.sprite.Group()
        self.instructionGroup = pygame.sprite.Group()
        
        self.starList = []
        
        #add static stars
        for star in range(125):
            starCoordsX = random.randrange(0,self.width)
            starCoordsY = random.randrange(0,self.height)
            self.starList.append((starCoordsX,starCoordsY))
        
        #tentacle variables
        self.divisions = 120
        self.tentaclesMin = 35
        self.tentaclesMax = 45
        
        parasiteNew = Parasite() 
        self.parasite.add(parasiteNew)
        
        parasiteTitleNew = Parasite()
        self.parasiteTitle.add(parasiteTitleNew)
        
        titleNew = Title()
        self.titleGroup.add(titleNew)
        
        instructionsNew = Instructions()
        self.instructionGroup.add(instructionsNew)
        
    def drawInstructions(self,screen):
        print ('drawinstructions screen is on')
        self.screen.fill(self.bgColor)
        w,h,m = self.width,self.height,self.margin
        
        print (self.instructionsPage)
        if self.instructionsPage == 1:
            titleFont = pygame.font.Font("DINPro.otf", 30)
            titleText = titleFont.render('how to play', True, WHITE)
            titleRect = titleText.get_rect()
            titleRect.centerx = self.width//2
            titleRect.centery = (self.height//10)*1
            
            parasiteFont = pygame.font.Font("DINPro.otf", 22)
            parasiteText = parasiteFont.render('this is you', True, WHITE)
            parasiteRect = parasiteText.get_rect()
            parasiteRect.left = (self.width//10)*2
            parasiteRect.centery = (self.height//10)*3
            
            planetFont = pygame.font.Font("DINPro.otf", 22)
            planetText = planetFont.render('these are planets', True, WHITE)
            planetRect = planetText.get_rect()
            planetRect.left = (self.width//10)*2
            planetRect.centery = (self.height//10)*6
            
            
            #draw parasite
            px = (self.width//10)*7
            py = (self.height//10)*3
            pygame.draw.circle(self.screen, WHITE,(px,py), parasiteSize, 5) #draw parasite
            for div in range(self.divisions):
                divAngle = div*((math.pi*2)/self.divisions)
                self.length = random.randrange(self.tentaclesMin,self.tentaclesMax)
                outerDivX = px + ((parasiteSize+self.length) * math.cos(divAngle))
                outerDivY = py + ((parasiteSize+self.length) * math.sin(divAngle))
                innerDivX = px + ((parasiteSize+6) * math.cos(divAngle))
                innerDivY = py + ((parasiteSize+6) * math.sin(divAngle))
                pygame.draw.line(self.screen,WHITE,(innerDivX,innerDivY), (outerDivX, outerDivY), 1)
            
            #draw little planets
            pygame.draw.circle(self.screen, WHITE,
                            ((self.width//60)*40,(self.height//30)*19), 
                            planetSize, 2) #draw planet top left
            pygame.draw.circle(self.screen, WHITE,
                            ((self.width//60)*45,(self.height//30)*18), 
                            planetSize, 2) #draw planet top right 
            pygame.draw.circle(self.screen, WHITE,
                            ((self.width//60)*46,(self.height//30)*20), 
                            planetSize, 2) #draw planet
            
            #draw text
            self.screen.blit(titleText, titleRect)
            self.screen.blit(parasiteText, parasiteRect)
            self.screen.blit(planetText, planetRect)
            
        if self.instructionsPage == 2:
            titleFont = pygame.font.Font("DINPro.otf", 30)
            titleText = titleFont.render('shit', True, WHITE)
            titleRect = titleText.get_rect()
            titleRect.centerx = screenWidth//2
            titleRect.centery = screenHeight//8
            self.screen.blit(titleText, titleRect)
        
    def drawSplash(self,screen):
        print ('drawsplash screen is on')
        self.screen.fill(self.bgColor)
        w,h,m = self.width,self.height,self.margin
        
        for star in self.starList:
            pygame.draw.circle(self.screen, DARKGREY,(star[0],star[1]),2)
            
        self.titleGroup.draw(screen)
        
        pygame.draw.circle(self.screen, WHITE,(self.tw//2,self.th//2), parasiteSize, 5) #draw parasite
        for div in range(self.divisions):
            divAngle = div*((math.pi*2)/self.divisions)
            self.length = random.randrange(self.tentaclesMin,self.tentaclesMax)
            outerDivX = self.tw//2 + ((parasiteSize+self.length) * math.cos(divAngle))
            outerDivY = self.th//2 + ((parasiteSize+self.length) * math.sin(divAngle))
            innerDivX = self.tw//2 + ((parasiteSize+6) * math.cos(divAngle))
            innerDivY = self.th//2 + ((parasiteSize+6) * math.sin(divAngle))
            pygame.draw.line(self.screen,WHITE,(innerDivX,innerDivY), (outerDivX, outerDivY), 1)
            
        #bouncing off walls
        if self.tw + (2*(parasiteSize+self.tentaclesMax)) >= self.width*2:
            print ('its too far to the left')
            self.hSpeed *= -1
        if self.tw - (2*(parasiteSize+self.tentaclesMax)) <= 0:
            print ('its too far to the right')
            self.hSpeed *= -1
        if self.th + (2*(parasiteSize+self.tentaclesMax)) >= self.height*2:
            print ('its too far up')
            self.vSpeed *= -1
        if self.th - (2*(parasiteSize+self.tentaclesMax)) <= 0:
            print ('its too far down')
            self.vSpeed *= -1
            
        
    def drawGame(self, screen):
        print ('drawgame is on')
        self.screen.fill(self.bgColor)
        w,h,m = self.width,self.height,self.margin
        font = pygame.font.Font("DINPro.otf", 20)
        textScore = font.render('score: %d   lives: %d' % (self.score,self.lives), True, WHITE)
        textScorerect = textScore.get_rect()
        textScorerect.centerx,textScorerect.centery = w//2, h-(m//2)
        textTitle = font.render("planet parasite", True, WHITE)
        textTitlerect = textTitle.get_rect()
        textTitlerect.centerx,textTitlerect.centery = w//2, (m//2)
        
        #add inhabited planets
        if self.frameCount % 60 == 0:
            inhabitedNew = Inhabited()
            self.inhabitedGroup.add(inhabitedNew)
            print ('new uninhabited')
        
        #add a planet every so often
        if self.frameCount % 60 == 0: 
            planet = Planet()
            self.planetGroup.add(planet)
            print ('new planet')
        
        for parasite in self.parasite:
            collisionPlanetsList = pygame.sprite.spritecollide(parasite,self.planetGroup,  False, 
                            pygame.sprite.collide_circle)
            for capturedPlanet in collisionPlanetsList:
                self.planetGroup.remove(capturedPlanet)
                self.score += 10
                capturedNew = Captured(w//2+random.randrange(-(parasiteSize-(1.5*planetSize)),(parasiteSize-(1.5*planetSize))),h//2+random.randrange(-(parasiteSize-(1.5*planetSize)),(parasiteSize-(1.5*planetSize))))
                self.capturedGroup.add(capturedNew)
            collisionInhabitedList = pygame.sprite.spritecollide(parasite,self.formedInhabitedGroup,  False, 
                            pygame.sprite.collide_circle)
            for hitInhabited in collisionInhabitedList:
                hitInhabited.stopUpdating(PINK) #turn the hit inhabited planet pink for right now 
                self.formedInhabitedGroup.remove(hitInhabited) #remove inhabited 
                self.lives -= 1
        
        # change length of tentacles based on lives
        if self.lives == 4:
            self.tentaclesMin = 25
            self.tentaclesMax = 35
        if self.lives == 3:
            self.tentaclesMin = 15
            self.tentaclesMax = 25
        if self.lives == 2:
            self.tentaclesMin = 5
            self.tentaclesMax = 15
        if self.lives == 1:
            self.tentaclesMin = 3
            self.tentaclesMax = 6
        if self.lives == 0:
            self.tentaclesMin = 999
            self.tentaclesMax = 1000
            self.gamePlay = False
            
        if self.frameCount % 5 == 0: #inhabited planets get larger and larger as time goes on
            for inhabited in self.inhabitedGroup:
                #if inhabited planet gets larger than a certain size
                if (inhabited.inhabitedSize >= .15*min(inhabited.imageX,inhabited.imageY)):
                    inhabited.stopUpdating(WHITE)
                    inhabited.dotted()
                    self.formedInhabitedGroup.add(inhabited)
                    self.inhabitedGroup.remove(inhabited)
                else:
                    inhabited.update()
        
        self.capturedGroup.update()
        for captured in self.capturedGroup:
            angle = math.atan(captured.coordsY/captured.coordsX)
            if captured.speed > 0:
                length = (captured.coordsY-h//2)/math.sin(angle)
                if (length >= parasiteSize-(1.5*planetSize)):
                    
                    captured.speed *= -1
            elif captured.speed < 0:
                length = (h//2-captured.coordsY)/math.sin(angle)
                if (length >= parasiteSize-(1.5*planetSize)):
                    
                    captured.speed *= -1
            
        self.parasite.update(self.tentaclesMax-7) #reduce radius by a few pixels to get make appearance better
        
        #DRAW STATEMENTS
        self.capturedGroup.draw(screen)
        self.planetGroup.draw(screen)
        self.inhabitedGroup.draw(screen)
        self.formedInhabitedGroup.draw(screen)
        self.parasite.draw(screen)
        
        for star in self.starList:
            pygame.draw.circle(self.screen, DARKGREY,(star[0],star[1]),2)
        
        for div in range(self.divisions):
            divAngle = div*((math.pi*2)/self.divisions)
            self.length = random.randrange(self.tentaclesMin,self.tentaclesMax)
            outerDivX = w//2 + ((parasiteSize+self.length) * math.cos(divAngle))
            outerDivY = h//2 + ((parasiteSize+self.length) * math.sin(divAngle))
            innerDivX = w//2 + ((parasiteSize+6) * math.cos(divAngle))
            innerDivY = h//2 + ((parasiteSize+6) * math.sin(divAngle))
            pygame.draw.line(self.screen,WHITE,(innerDivX,innerDivY), (outerDivX, outerDivY), 1)
            # tentacleNew = Tentacle(innerDivX,innerDivY,outerDivX,outerDivY)
            # self.tentacleGroup.add(tentacleNew)
        
        # pygame.draw.rect(screen, CHARCOAL,(0, 0, w, m)) #border top rect
        # pygame.draw.rect(screen, CHARCOAL,(0, 0, m, h)) #border bottom rect
        # pygame.draw.rect(screen, CHARCOAL,(w-m, 0, m, h)) #border top rect
        # pygame.draw.rect(screen, CHARCOAL,(0, h-m, w, m)) #border top rect
        # 
        # pygame.draw.rect(screen, WHITE,(m,m, w-(2*m),h-(2*m)), 2) #border
        screen.blit(textScore, textScorerect)
        screen.blit(textTitle, textTitlerect)

Game(screenWidth, screenHeight).run()