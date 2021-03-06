'''
pygamegame.py

'''
import pygame
import sys
import random
from pygame.locals import *
from gVariables import *



class PygameGame(object):

    def init(self):
        pass
    # def mousePressed(self, x, y):
    #     pass

   ##   def mouseReleased(self, x, y):
    #     pass

   ##   def mouseMotion(self, x, y):
    #     pass

   ##   def mouseDrag(self, x, y):
    #     pass

   ##   def keyPressed(self, keyCode, modifier):
    #     pass

   ##   def keyReleased(self, keyCode, modifier):
    #     pass

   ##   def timerFired(self, dt):
    #     pass

    def drawEndScreen(self, screen):
        pass

    def drawGame(self, screen):
        pass
    
    def drawSplash(self, screen):
        pass
    
    def drawInstructions(self,screen):
        pass
        
    def __init__(self, width=screenWidth, height=screenHeight, fps=60, title="PLANET PARASITE"):
        self.width, self.height = width, height
        self.playing = False
        self.margin= self.width//10
        self.fps = fps
        self.title = title
        self.bgColor = CHARCOAL
        self.score = 0
        self.totalSeconds = 0
        self.frameCount = 0
        self.frameRate = 60
        self.startTime = 0
        self.speed = 22
        self.lives = 1
        self.hSpeed = 0 #acceleration horizontally
        self.vSpeed = 0 #acceleration vertically
        self.gamePlay = False
        self.instructions = False
        self.instructionsPage = 1
        self.tw = self.width
        self.th = self.height
        self.attack = False
        self.attackMeter = 100
        self.tentacleColor = WHITE
        self.divisions = 120
        self.tentaclesMin = 35
        self.tentaclesMax = 45
        self.parasiteSize = parasiteSize
        self.highScore = 0
        
        self.eatMeStop = "empty"
        self.eatMeInv = "empty"
        self.eatMeTen = "empty"
        self.eatMeStopCount = 0
        self.eatMeTenCount = 0
        self.eatMeCurr = 1
        self.eatMeCurrLine = 3
        
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        w,h,m = self.width,self.height,self.margin
        self.screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)
        
        # call game-specific initialization
        self.init()
        self.playing = True
        
        #for moving around
        left = False
        right = False
        up = False
        down = False
        
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if (event.type == pygame.KEYDOWN) and (event.key == K_LEFT):
                    left = True
                    if self.instructions == True:
                        self.instructionsPage -= 1
                        self.instructionsPage = max(self.instructionsPage,1) #prevent negative pages
                if (event.type == pygame.KEYUP) and (event.key == K_LEFT):
                    left = False
                if (event.type == pygame.KEYDOWN) and (event.key == K_RIGHT):
                    right = True
                    if self.instructions == True:
                        self.instructionsPage += 1
                if (event.type == pygame.KEYUP) and (event.key == K_RIGHT):
                    right = False
                if (event.type == pygame.KEYDOWN) and (event.key == K_UP):
                    up = True
                if (event.type == pygame.KEYUP) and (event.key == K_UP):
                    up = False
                if (event.type == pygame.KEYDOWN) and (event.key == K_DOWN):
                    down = True
                if (event.type == pygame.KEYUP) and (event.key == K_DOWN):
                    down = False
                if (event.type == pygame.KEYDOWN) and (event.key == K_SPACE):
                    if not self.instructions and not self.gamePlay:
                        self.hSpeed = 0
                        self.vSpeed = 0
                        self.score = 0
                        self.lives = 5
                        self.attackMeter = 100
                        self.gamePlay = True
                if (event.type == pygame.KEYDOWN) and (event.key == K_h):
                    if not self.gamePlay:
                        self.instructionsPage = 1 #reset instruction page to 1
                        self.instructions = True
                #attack mode
                if (event.type == pygame.KEYDOWN) and (event.key == K_1): 
                    if self.attackMeter > 0:
                        self.attack = True
                    if self.attackMeter <= 0: #attack meter runs out
                        self.attack = False
                if (event.type == pygame.KEYUP) and (event.key == K_1):
                    self.attack = False
                if (event.type == pygame.KEYDOWN) and (event.key == K_2):
                    if self.eatMeCurr == 1 and self.eatMeStop == "collected":
                        self.eatMeStop = "enabled"
                    if self.eatMeCurr == 2 and self.eatMeInv == "collected":
                        self.eatMeInv = "enabled"
                    if self.eatMeCurr == 3 and self.eatMeTen == "collected":
                        self.eatMeTen = "enabled"
                if (event.type == pygame.KEYDOWN) and (event.key == K_w):
                    self.eatMeCurr += 1
                    self.eatMeCurr = min(self.eatMeCurr,3)
                if (event.type == pygame.KEYDOWN) and (event.key == K_s):
                    self.eatMeCurr -= 1
                    self.eatMeCurr = max(self.eatMeCurr,1)
                if (event.type == pygame.KEYDOWN) and (event.key == K_ESCAPE):
                    self.gamePlay = False
                    
            self.planetGroup.clear(self.screen,clear_callback)
            self.parasite.clear(self.screen,clear_callback)
            self.inhabitedGroup.clear(self.screen,clear_callback)
            self.formedInhabitedGroup.clear(self.screen,clear_callback)
            self.titleGroup.clear(self.screen,clear_callback)
            self.parasiteTitle.clear(self.screen,clear_callback)
            self.instructionsInhabited.clear(self.screen,clear_callback)
            
            if left and self.hSpeed < self.speed:
                self.hSpeed += 1
            if right and self.hSpeed > (-1*self.speed):
                self.hSpeed -= 1
            if up and self.vSpeed < self.speed: 
                self.vSpeed += 1
            if down and self.vSpeed > (-1*self.speed): 
                self.vSpeed -= 1
                
            #if game is on
            if self.gamePlay: 
                self.drawGame(self.screen)
                for planet in self.planetGroup:
                    planet.move(self.hSpeed,self.vSpeed)
                for inhabited in self.inhabitedGroup:
                    inhabited.move(self.hSpeed,self.vSpeed)
                for inhabited in self.formedInhabitedGroup:
                    inhabited.move(self.hSpeed,self.vSpeed)
                for parasite in self.parasiteTitle:
                    parasite.move(self.hSpeed,self.vSpeed)
                for eatMeStop in self.eatMeStopGroup:
                    eatMeStop.move(self.hSpeed,self.vSpeed)
                for eatMeInv in self.eatMeInvGroup:
                    eatMeInv.move(self.hSpeed,self.vSpeed)
                for eatMeTen in self.eatMeTenGroup:
                    eatMeTen.move(self.hSpeed,self.vSpeed)
                for eatMeLife in self.eatMeLifeGroup:
                    eatMeLife.move(self.hSpeed,self.vSpeed)
                    
            #if splash screen on
            if not self.gamePlay and not self.instructions:
                self.drawSplash(self.screen)
                self.th -= self.vSpeed
                self.tw -= self.hSpeed
                
            #if splash screen on
            if not self.gamePlay and self.instructions: 
                self.drawInstructions(self.screen)
                 
            
            basicfont = pygame.font.Font("DINPro.otf", 20)
            
            self.frameCount += 1
            
            # Limit frames per second
            clock.tick(self.frameRate)
            
            pygame.display.flip()
            
        pygame.quit()
        print ('So long!')

def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
