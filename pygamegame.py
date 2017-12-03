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

    def __init__(self, width=600, height=800, fps=50, title="PLANET PARASITE"):
        self.width, self.height = width, height
        self.margin= self.width//8
        self.fps = fps
        self.title = title
        self.score = 0
        self.totalSeconds = 0
        self.frameCount = 0
        self.frameRate = 60
        self.startTime = 90
        self.speed = 15
        self.borderX0 = -self.width
        self.borderY0 = -self.height
        self.collisions = 0
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        w,h,m = self.width,self.height,self.margin
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        
        left = False
        right = False
        
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if (event.type == pygame.KEYDOWN) and (event.key == K_LEFT):
                    # print ('left key')
                    for planet in self.planetGroup:
                        planet.move(self.speed,0)
                    self.borderX0 = self.borderX0 + self.speed
                if (event.type == pygame.KEYDOWN) and (event.key == K_RIGHT):
                    # print ('right key')
                    for planet in self.planetGroup:
                        planet.move(-self.speed,0)
                    self.borderX0 = self.borderX0 - self.speed
                if (event.type == pygame.KEYDOWN) and (event.key == K_UP):
                    # print ('up key')
                    for planet in self.planetGroup:
                        planet.move(0,self.speed)
                    self.borderY0 = self.borderY0 + self.speed
                if (event.type == pygame.KEYDOWN) and (event.key == K_DOWN):
                    # print ('down key')
                    for planet in self.planetGroup:
                        planet.move(0,-self.speed)
                    self.borderY0 = self.borderY0 - self.speed
                if (event.type == pygame.KEYDOWN) and (event.key == K_ESCAPE):
                    playing = False
            
            screen.fill(CHARCOAL)
            self.redrawAll(screen)
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
            screen.blit(text, [250, 250])
            
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
