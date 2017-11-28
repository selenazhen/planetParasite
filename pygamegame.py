'''
pygamegame.py

'''
import pygame
import sys
from pygame.locals import *
# from Planet import Planet, planetCoordsX,planetCoordsY

CHARCOAL = (31,31,31)
WHITE = (255,255,255)
BLACK = (0,0,0)

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

    def __init__(self, width=600, height=800, fps=100, title="PLANET PARASITE"):
        self.width, self.height = width, height
        self.margin= self.width//8
        self.fps = fps
        self.title = title
        self.parasiteX = self.width//2
        self.parasiteY = self.height//2
        self.speed = 25
        self.score = 0
        self.totalSeconds = 0
        self.frameCount = 0
        self.frameRate = 60
        self.startTime = 90
        # self.planetList = pygame.sprite.Group()
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
                if (event.type == pygame.KEYDOWN) and (event.key == K_LEFT):
                    # for planet in self.planetList:
                    #     planet[0] -= self.speed
                    planet.moveLeft()
                elif (event.type == pygame.KEYDOWN) and (event.key == K_RIGHT):
                    # for planet in self.planetList:
                    #     planet[0] += self.speed
                    planet.moveRight()
                elif (event.type == pygame.KEYDOWN) and (event.key == K_UP):
                    # for planet in self.planetList:
                    #     planet[1] -= self.speed
                    planet.moveUp()
                elif (event.type == pygame.KEYDOWN) and (event.key == K_DOWN):
                    # for planet in self.planetList:
                    #     planet[1] += self.speed
                    planet.moveDown()
                if (event.type == pygame.KEYDOWN) and (event.key == K_ESCAPE):
                    playing = False
                elif event.type == pygame.QUIT:
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
