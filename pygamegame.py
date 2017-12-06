'''
pygamegame.py

'''
import pygame
import sys
import random
from pygame.locals import *
from gVariables import *
from Tentacles import Tentacle

class PygameGame(object):

    def init(self):
        pass
    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        pass

    def isKeyPressed(self, key):
        return self._keys.get(key, False)

    def __init__(self, width=screenWidth, height=screenHeight, fps=100, title="PLANET PARASITE"):
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
        self.speed = 14
        self.borderX0 = -self.width
        self.borderY0 = -self.height
        self.collisions = 0
        self.keyCont = False
        self.lives = 5
        self.hSpeed = 0
        self.vSpeed = 0
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        w,h,m = self.width,self.height,self.margin
        self.screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

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
                    # self.hSpeed += 1
                    # print (self.hSpeed)
                if (event.type == pygame.KEYUP) and (event.key == K_LEFT):
                    left = False
                if (event.type == pygame.KEYDOWN) and (event.key == K_RIGHT):
                    right = True
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
                if (event.type == pygame.KEYDOWN) and (event.key == K_ESCAPE):
                    playing = False
            
            if left and self.hSpeed < self.speed:
                self.hSpeed += 0.4
                
            if right and self.hSpeed > (-1*self.speed):
                self.hSpeed -= 0.4
            if up and self.vSpeed < self.speed: 
                self.vSpeed += 0.4
            if down and self.vSpeed > (-1*self.speed): 
                self.vSpeed -= 0.4
            
            for planet in self.planetGroup:
                planet.move(self.hSpeed,self.vSpeed)
            for inhabited in self.inhabitedGroup:
                inhabited.move(self.hSpeed,self.vSpeed)
            for inhabited in self.formedInhabitedGroup:
                inhabited.move(self.hSpeed,self.vSpeed)
            
            self.redrawAll(self.screen)
            

            basicfont = pygame.font.Font("DINPro.otf", 20)

            # --- Timer going up ---
            # Calculate total seconds
            self.totalSeconds = self.frameCount // self.frameRate
        
            # Divide by 60 to get total minutes
            minutes = self.totalSeconds // 60
        
            # Use modulus (remainder) to get seconds
            seconds = self.totalSeconds % 60
        
            # Use python string formatting to format in leading zeros
            # output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
            output_string = "Temp: Seconds: {0:01}".format(self.totalSeconds)
        
            # Blit to the screen
            text = basicfont.render(output_string, True, WHITE)
            # screen.blit(text, [250, 250])
            
            '''
            # --- Timer going down ---
            # Calculate total seconds
            self.totalSeconds = startTime - (self.frameCount // self.frameRate)
            if self.totalSeconds < 0:
                self.totalSeconds = 0
        
            # Divide by 60 to get total minutes
            minutes = self.totalSeconds // 60
        
            # Use modulus (remainder) to get seconds
            seconds = self.totalSeconds % 60
        
            # Use python string formatting to format in leading zeros
            output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
        
            # Blit to the screen
            text = basicfont.render(output_string, True, WHITE)
        
            screen.blit(text, [250, 280])
            '''
        
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
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
