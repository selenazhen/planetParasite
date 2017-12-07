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
edit drawing functions here
'''

class Game(PygameGame):
    def init(self):
        self.shield = pygame.image.load('img/shield.png').convert_alpha()
        self.tentImage = pygame.image.load('img/tentacles.png').convert_alpha()
        
        self.planetGroup = pygame.sprite.Group()
        self.parasite = pygame.sprite.Group()
        self.inhabitedGroup = pygame.sprite.Group()
        self.formedInhabitedGroup = pygame.sprite.Group()
        # self.capturedGroup = pygame.sprite.Group()
        self.eatMeInvGroup = pygame.sprite.Group()
        self.eatMeStopGroup = pygame.sprite.Group()
        
        self.titleGroup = pygame.sprite.Group()
        self.parasiteTitle = pygame.sprite.Group()
        self.instructionsInhabited = pygame.sprite.Group()
        
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
    
        parasiteNew = Parasite(self.parasiteSize) 
        self.parasite.add(parasiteNew)
        
        parasiteTitleNew = Parasite(self.parasiteSize)
        self.parasiteTitle.add(parasiteTitleNew)
        
        titleNew = Title()
        self.titleGroup.add(titleNew)
        
        inhabitedTitleNew = Inhabited((self.width//20)*27,(self.height//10)*15)
        self.instructionsInhabited.add(inhabitedTitleNew)
        self.formed = False
        
    def drawInstructions(self,screen):
        print ('drawinstructions screen is on')
        screen.fill(self.bgColor)
        w,h,m = self.width,self.height,self.margin
        
        if self.instructionsPage == 1:
            titleFont = pygame.font.Font("DINPro.otf", 30)
            titleText = titleFont.render('how to play', True, WHITE)
            titleRect = titleText.get_rect()
            titleRect.centerx = self.width//2
            titleRect.centery = (self.height//20)*2
            
            parasiteFont = pygame.font.Font("DINPro.otf", 19)
            parasiteText = parasiteFont.render("this is you (a parasite)", True, WHITE)
            parasiteRect = parasiteText.get_rect()
            parasiteRect.left = (self.width//40)*5
            parasiteRect.centery = (self.height//20)*6
            
            planetFont = pygame.font.Font("DINPro.otf", 19)
            planetText = planetFont.render('these are uninhabited planets', True, WHITE)
            planetRect = planetText.get_rect()
            planetRect.left = (self.width//40)*5
            planetRect.centery = (self.height//20)*11
            
            inhabitedFont = pygame.font.Font("DINPro.otf", 19)
            if not self.formed:
                inhabitedText = inhabitedFont.render('this is a developing planet', True, WHITE)
            if self.formed: 
                inhabitedText = inhabitedFont.render('this is an inhabited planet', True, WHITE)
            inhabitedRect = inhabitedText.get_rect()
            inhabitedRect.left = (self.width//40)*5
            inhabitedRect.centery = (self.height//20)*16
        
            
            if self.frameCount >= 60 and self.frameCount % 3 == 0: #inhabited planets get larger and larger as time goes on
                for inhabited in self.instructionsInhabited:
                    #if inhabited planet gets larger than a certain size:
                    if (inhabited.inhabitedSize >= .06*min(inhabited.imageX,inhabited.imageY)):
                        inhabited.stopUpdating(WHITE)
                        inhabited.dotted()
                        self.formedInhabitedGroup.add(inhabited)
                        self.instructionsInhabited.remove(inhabited)
                        self.formed = True
                    else:
                        inhabited.update()
                        
            #draw parasite
            px = (self.width//20)*15
            py = (self.height//10)*3
            pygame.draw.circle(screen, WHITE,(px,py), self.parasiteSize, 5) #draw parasite
            for div in range(self.divisions):
                divAngle = div*((math.pi*2)/self.divisions)
                self.length = random.randrange(self.tentaclesMin,self.tentaclesMax)
                outerDivX = px + ((self.parasiteSize+self.length) * math.cos(divAngle))
                outerDivY = py + ((self.parasiteSize+self.length) * math.sin(divAngle))
                innerDivX = px + ((self.parasiteSize+6) * math.cos(divAngle))
                innerDivY = py + ((self.parasiteSize+6) * math.sin(divAngle))
                pygame.draw.line(screen,WHITE,(innerDivX,innerDivY), (outerDivX, outerDivY), 1)
            
            #draw little planets
            pygame.draw.circle(screen, WHITE,
                            ((self.width//60)*42,(self.height//30)*17), 
                            planetSize, 2) #draw planet top left
            pygame.draw.circle(screen, WHITE,
                            ((self.width//60)*47,(self.height//30)*16), 
                            planetSize, 2) #draw planet top right 
            pygame.draw.circle(screen, WHITE,
                            ((self.width//60)*48,(self.height//30)*18), 
                            planetSize, 2) #draw planet
            
            #draw text
            self.instructionsInhabited.draw(screen)
            self.formedInhabitedGroup.draw(screen)
            screen.blit(titleText, titleRect)
            screen.blit(parasiteText, parasiteRect)
            screen.blit(planetText, planetRect)
            screen.blit(inhabitedText, inhabitedRect)
            
        if self.instructionsPage == 2: #second instructions page
            titleFont = pygame.font.Font("DINPro.otf", 30)
            titleText = titleFont.render('how to play', True, WHITE)
            titleRect = titleText.get_rect()
            titleRect.centerx = self.width//2
            titleRect.centery = (self.height//20)*2
            
            parFont = pygame.font.Font("DINPro.otf", 20)
            
            text1 = wrapline("capture the uninhabited planets and the developing planets but avoid the fully formed inhabited planets.", parFont, 475)
            text2 = wrapline("for every time you are caught within the safety zone of an inhabited planet you lose a life and your tentacles shorten.", parFont, 475)
            text3 = wrapline("look for planets with powerups to help improve your parasitic nature.", parFont, 475)
            
            lineSpacing = self.height//30
            for i in range(len(text1)):
                parText = parFont.render(text1[i], True, WHITE)
                parRect = parText.get_rect()
                parRect.left = (self.width//40)*5
                parRect.centery = (self.height//40)*8 + (lineSpacing*i)
                screen.blit(parText, parRect)
            
            for i in range(len(text2)):
                parText = parFont.render(text2[i], True, WHITE)
                parRect = parText.get_rect()
                parRect.left = (self.width//40)*5
                parRect.centery = (self.height//40)*12 + (lineSpacing*i)
                screen.blit(parText, parRect)
                
            for i in range(len(text3)):
                parText = parFont.render(text3[i], True, WHITE)
                parRect = parText.get_rect()
                parRect.left = (self.width//40)*5
                parRect.centery = (self.height//40)*17 + (lineSpacing*i)
                screen.blit(parText, parRect)
            
            screen.blit(titleText, titleRect)
            screen.blit(parText, parRect)
        if self.instructionsPage == 3:
            self.instructions = False

    def drawSplash(self,screen):
        # print ('drawsplash screen is on')
        screen.fill(self.bgColor)
        w,h,m = self.width,self.height,self.margin
        
        for star in self.starList:
            pygame.draw.circle(screen, DARKGREY,(star[0],star[1]),2)
            
        nameFont = pygame.font.Font("DINPro.otf", 16)
        nameText = nameFont.render('by selena zhen', True, WHITE)
        nameRect = nameText.get_rect()
        nameRect.centerx = (self.width//2)
        nameRect.centery = (self.height//20)*18
        
        pygame.draw.circle(screen, WHITE,(self.tw//2,self.th//2), self.parasiteSize, 5) #draw parasite
        for div in range(self.divisions):
            divAngle = div*((math.pi*2)/self.divisions)
            self.length = random.randrange(self.tentaclesMin,self.tentaclesMax)
            outerDivX = self.tw//2 + ((self.parasiteSize+self.length) * math.cos(divAngle))
            outerDivY = self.th//2 + ((self.parasiteSize+self.length) * math.sin(divAngle))
            innerDivX = self.tw//2 + ((self.parasiteSize+6) * math.cos(divAngle))
            innerDivY = self.th//2 + ((self.parasiteSize+6) * math.sin(divAngle))
            pygame.draw.line(screen,WHITE,(innerDivX,innerDivY), (outerDivX, outerDivY), 1)
            
        #bouncing off walls
        if self.tw + (2*(self.parasiteSize+self.tentaclesMax)) >= self.width*2:
            print ('its too far to the left')
            self.hSpeed *= -1
        if self.tw - (2*(self.parasiteSize+self.tentaclesMax)) <= 0:
            print ('its too far to the right')
            self.hSpeed *= -1
        if self.th + (2*(self.parasiteSize+self.tentaclesMax)) >= self.height*2:
            print ('its too far up')
            self.vSpeed *= -1
        if self.th - (2*(self.parasiteSize+self.tentaclesMax)) <= 0:
            print ('its too far down')
            self.vSpeed *= -1
            
        self.titleGroup.draw(screen)
        screen.blit(nameText, nameRect)
        
    def drawGame(self, screen):
        screen.fill(self.bgColor)
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
            inhabitedNew = Inhabited(0,0)
            self.inhabitedGroup.add(inhabitedNew)
            # print ('new uninhabited')
        
        #add a planet every so often
        if self.frameCount % 60 == 0: 
            planet = Planet(2,WHITE)
            self.planetGroup.add(planet)
            # print ('new planet')
            
        #add eat me powerups
        if self.frameCount % random.randrange(500,700) == 0:
            eatMeColors = [YELLOW,BLUE]
            eatMe = Planet(0,random.choice(eatMeColors))
            if eatMe.color == YELLOW: #if invincibility planet
                self.eatMeInvGroup.add(eatMe)
            elif eatMe.color == BLUE: #if stop
                self.eatMeStopGroup.add(eatMe)
        
        for parasite in self.parasite:
            if self.attack:
                collisionAttackList = pygame.sprite.spritecollide(parasite,self.inhabitedGroup,  False, 
                                pygame.sprite.collide_circle)
                for attacked in collisionAttackList:
                    self.inhabitedGroup.remove(attacked)
            
            elif not self.attack: # if attack mode off and invincibility not enabled
                #if collide with a planet
                collisionPlanetsList = pygame.sprite.spritecollide(parasite,self.planetGroup,  False, 
                                pygame.sprite.collide_circle)
                for capturedPlanet in collisionPlanetsList:
                    self.planetGroup.remove(capturedPlanet)
                    self.score += 10
                #if collided with eat me stop
                collisionEatMeStopList = pygame.sprite.spritecollide(parasite,self.eatMeStopGroup,  False, 
                                pygame.sprite.collide_circle)
                for eatMeStop in collisionEatMeStopList:
                    self.eatMeStopGroup.remove(eatMeStop)
                    self.eatMeStop = "collected"
                    print ('eat me stop collected')
                #if collide with eat me invincible
                collisionEatMeInvList = pygame.sprite.spritecollide(parasite,self.eatMeInvGroup,  False, 
                                pygame.sprite.collide_circle)
                for eatMeInv in collisionEatMeInvList:
                    self.eatMeInvGroup.remove(eatMeInv)
                    self.eatMeInv = "collected"
                    print ('eat me inv collected')
                #if invincibility is not on, inhabited can harm parasite
                if not self.eatMeInv == "enabled": 
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
            
        self.parasite.update(self.tentaclesMax-7) #reduce radius by a few pixels to get make appearance better
        
        self.inhabitedGroup.draw(screen) #keep this at bottom of draw statements
        
        #DRAW STATEMENTS
        # self.capturedGroup.draw(screen) #THIS IS MAKING IT SLOW :((((
        self.planetGroup.draw(screen)
        self.formedInhabitedGroup.draw(screen)
        self.parasite.draw(screen)
        self.eatMeInvGroup.draw(screen)
        self.eatMeStopGroup.draw(screen)
        
        for div in range(self.divisions):
            divAngle = div*((math.pi*2)/self.divisions)
            self.length = random.randrange(self.tentaclesMin,self.tentaclesMax)
            outerDivX = w//2 + ((self.parasiteSize+self.length) * math.cos(divAngle))
            outerDivY = h//2 + ((self.parasiteSize+self.length) * math.sin(divAngle))
            innerDivX = w//2 + ((self.parasiteSize+6) * math.cos(divAngle))
            innerDivY = h//2 + ((self.parasiteSize+6) * math.sin(divAngle))
            pygame.draw.line(screen,self.tentacleColor,(innerDivX,innerDivY), (outerDivX, outerDivY), 1)
        
        # eatMeStop discontinue growth of developing planets BLUE 1
        eSX = self.width//20
        eSY = (self.height//28)*19
        if self.eatMeStop == "collected":
            pygame.draw.rect(screen,BLUE,(eSX-20,eSY,40,40))
        if self.eatMeStop == "enabled":
            self.eatMeStopCount += 1
            pygame.draw.rect(screen,RED,(eSX-20,eSY,40,40))
            if self.eatMeStopCount >= 100: #timer ends for eatme powerup
                self.eatMeStop = "empty"
                self.eatMeStopCount = 0
        if (self.eatMeStop == "empty"):
            pygame.draw.rect(screen,CHARCOAL,(eSX-20,eSY,40,40))
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
        if self.eatMeCurr == 1: 
            pygame.draw.rect(screen,WHITE,(eSX-20,eSY,40,40),self.eatMeCurrLine)
        elif not self.eatMeCurr == 1: 
            pygame.draw.rect(screen,WHITE,(eSX-20,eSY,40,40),1)
        pygame.draw.circle(screen,GREY,(eSX,eSY+20),10,1)
        pygame.draw.line(screen,GREY,(eSX-7,eSY-7+20),(eSX+7,eSY+7+20),1)
        
        # eatMeInv invincibility YELLOW 2
        eIX = self.width//20
        eIY = (self.height//28)*17
        if self.eatMeInv == "collected":
            pygame.draw.rect(screen,YELLOW,(eIX-20,eIY,40,40))
        if self.eatMeInv == "enabled":
            self.eatMeStopCount += 1
            pygame.draw.rect(screen,RED,(eIX-20,eIY,40,40))
            if self.eatMeStopCount >= 100: #timer ends for eatme powerup
                self.eatMeInv = "empty"
                self.eatMeStopCount = 0
        if (self.eatMeInv == "empty"):
            pygame.draw.rect(screen,CHARCOAL,(eIX-20,eIY,40,40))
        if self.eatMeCurr == 2: 
            pygame.draw.rect(screen,WHITE,(eIX-20,eIY,40,40),self.eatMeCurrLine) #border box
        elif not self.eatMeCurr  == 2: 
            pygame.draw.rect(screen,WHITE,(eIX-20,eIY,40,40),1) #border box
        screen.blit(self.shield,(eIX-9,eIY+10))
        
        # eatMeTen increase tentacle lengths green 2
        eTX = self.width//20
        eTY = (self.height//28)*15
        if self.eatMeTen == "collected":
            pygame.draw.rect(screen,YELLOW,(eTX-20,eTY,40,40))
        if self.eatMeTen == "enabled":
            self.eatMeTenCount += 1
            pygame.draw.rect(screen,RED,(eTX-20,eTY,40,40))
            if self.eatMeTenCount >= 100: #timer ends for eatme powerup
                self.eatMeTen = "empty"
                self.eatMeTenCount = 0
        if (self.eatMeTen == "empty"):
            pygame.draw.rect(screen,CHARCOAL,(eTX-20,eTY,40,40))
        if self.eatMeCurr == 3: 
            pygame.draw.rect(screen,WHITE,(eTX-20,eTY,40,40),self.eatMeCurrLine) #border box
        elif not self.eatMeCurr  == 3: 
            pygame.draw.rect(screen,WHITE,(eTX-20,eTY,40,40),1) #border box
        pygame.draw.line(screen,GREY,(eTX,eTY+15),(eTX,eTY+25),1) #plus sign vertical
        pygame.draw.line(screen,GREY,(eTX-5,eTY+20),(eTX+5,eTY+20),1) #plus sign horizontal
        screen.blit(self.tentImage,(eTX-17,eTY+5))
        
        #attack stuff here
        if self.attack:
            self.tentacleColor = RED
            self.attackMeter -= 3 #reduce attack meter faster
            if self.attackMeter <= 0:
                self.attackMeter = 0 #keep attack meter at minimum of 0
        if not self.attack:
            self.tentacleColor = WHITE
            if self.frameCount % 30 == 0:#regain attack meter slowly
                self.attackMeter += 1 
                self.attackMeter = min(self.attackMeter,100) #keep attackmeter at max of 100
        aX = self.width//20
        aY0 = (self.height//14)*13
        aY1 = aY0 - (1.5*self.attackMeter)
        pygame.draw.rect(screen,WHITE,(aX-5,aY0-150,12,150),1) # border for bar
        if self.attackMeter > 0:
            pygame.draw.line(screen,self.tentacleColor,(aX,aY0), 
                        (aX, aY1), 12)
        elif self.attackMeter <= 0:
            pygame.draw.line(screen,self.tentacleColor,(aX,aY0), 
                        (aX, aY0), 12)
        attackFont = pygame.font.Font("DINPro.otf", 16)
        attackText = attackFont.render('%d' % (max(self.attackMeter,0)), True, WHITE)
        attackRect = attackText.get_rect()
        attackRect.centerx = aX
        attackRect.centery = aY0 + 15
        
        # pygame.draw.rect(screen, CHARCOAL,(0, 0, w, m)) #border top rect
        # pygame.draw.rect(screen, CHARCOAL,(0, 0, m, h)) #border bottom rect
        # pygame.draw.rect(screen, CHARCOAL,(w-m, 0, m, h)) #border top rect
        # pygame.draw.rect(screen, CHARCOAL,(0, h-m, w, m)) #border top rect
        #   
        # pygame.draw.rect(screen, WHITE,(m,m, w-(2*m),h-(2*m)), 2) #border
        
        # for star in self.starList:
        #     pygame.draw.circle(screen, DARKGREY,(star[0],star[1]),2)
        
        screen.blit(textScore, textScorerect)
        screen.blit(textTitle, textTitlerect)
        screen.blit(attackText, attackRect)

Game(screenWidth, screenHeight).run()