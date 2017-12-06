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
        self.startTime = 90
        self.speed = 10
        self.lives = 5
        self.hSpeed = 0 #acceleration horizontally
        self.vSpeed = 0 #acceleration vertically
        self.gamePlay = False
        self.instructions = False
        self.instructionsPage = 1
        self.tw = self.width
        self.th = self.height
        
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
                    self.gamePlay = True
                    print ('gameplay on')
                if (event.type == pygame.KEYDOWN) and (event.key == K_0):
                    self.gamePlay = False
                    self.instructions = False
                    print ('gameplay off')
                if (event.type == pygame.KEYDOWN) and (event.key == K_h):
                    self.gamePlay = False
                    self.instructionsPage = 1 #reset instruction page to 1
                    self.instructions = True
                    
                    print ('gameplay off')
                if (event.type == pygame.KEYDOWN) and (event.key == K_ESCAPE):
                    self.playing = False
            
            if left and self.hSpeed < self.speed:
                self.hSpeed += 1
            if right and self.hSpeed > (-1*self.speed):
                self.hSpeed -= 1
            if up and self.vSpeed < self.speed: 
                self.vSpeed += 1
            if down and self.vSpeed > (-1*self.speed): 
                self.vSpeed -= 1
                
            if self.gamePlay: #if game is on
                self.drawGame(self.screen)
                for planet in self.planetGroup:
                    planet.move(self.hSpeed,self.vSpeed)
                for inhabited in self.inhabitedGroup:
                    inhabited.move(self.hSpeed,self.vSpeed)
                for inhabited in self.formedInhabitedGroup:
                    inhabited.move(self.hSpeed,self.vSpeed)
                for parasite in self.parasiteTitle:
                    parasite.move(self.hSpeed,self.vSpeed)
                    
            if not self.gamePlay and not self.instructions: #if splash screen on
                self.drawSplash(self.screen)
                self.th -= self.vSpeed
                self.tw -= self.hSpeed
                
            if not self.gamePlay and self.instructions: #if splash screen on
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
