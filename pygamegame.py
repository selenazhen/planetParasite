'''
pygamegame.py
Citations: 
--General format: Lukas Peraza for 15-112 F15 Pygame Optional Lecture, 11/11/15
--Time Modules: http://programarcadegames.com/python_examples/f.php?file=timer.py

'''
import pygame
import sys
from pygame.locals import *

CHARCOAL = (31,31,31)
WHITE = (255,255,255)
BLACK = (0,0,0)

clock = pygame.time.Clock()
 

 


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
        # w,h,m = self.width,self.height,self.margin
        # basicfont = pygame.font.Font("DINPro.otf", 20)
        # textScore = basicfont.render('score: %d' % (self.score), True, WHITE)
        # textScorerect = textScore.get_rect()
        # textScorerect.centerx,textScorerect.centery = w//2, h-(m//2)
        # textTitle = basicfont.render("planet parasite", True, WHITE)
        # textTitlerect = textTitle.get_rect()
        # textTitlerect.centerx,textTitlerect.centery = w//2, (m//2)
        # 
       
#       #   pygame.draw.circle(screen, WHITE,(self.parasiteX,self.parasiteY),
        #                     m, 5) #testing circle
    
   #    #   pygame.draw.rect(screen, CHARCOAL,(0, 0, w, m)) #border top rect
        # pygame.draw.rect(screen, CHARCOAL,(0, 0, m, h)) #border bottom rect
        # pygame.draw.rect(screen, CHARCOAL,(w-m, 0, m, h)) #border top rect
        # pygame.draw.rect(screen, CHARCOAL,(0, h-m, w, m)) #border top rect
        # 
        # pygame.draw.rect(screen, WHITE,(m,m, w-(2*m),h-(2*m)), 2) #border
        # screen.blit(textScore, textScorerect)
        # screen.blit(textTitle, textTitlerect)
        pass

    def isKeyPressed(self, key):
        return self._keys.get(key, False)

    def __init__(self, width=600, height=800, fps=100, title="PLANET PARASITE"):
        self.width = width
        self.height = height
        self.margin= self.width//8
        self.fps = fps
        self.title = title
        self.parasiteX = self.width//2
        self.parasiteY = self.height//2
        self.speed = 25
        self.score = 0
        self.totalSeconds = 0
        pygame.init()

    def run(self):
        frame_count = 0
        frame_rate = 60
        start_time = 90
        w,h,m = self.width,self.height,self.margin
        
        clock = pygame.time.Clock()
        
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
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN) and (event.key == K_LEFT):
                    self.parasiteX -= self.speed
                elif (event.type == pygame.KEYDOWN) and (event.key == K_RIGHT):
                    self.parasiteX += self.speed
                elif (event.type == pygame.KEYDOWN) and (event.key == K_UP):
                    self.parasiteY -= self.speed
                elif (event.type == pygame.KEYDOWN) and (event.key == K_DOWN):
                    self.parasiteY += self.speed
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(CHARCOAL)
            self.redrawAll(screen)
            
            basicfont = pygame.font.Font("DINPro.otf", 20)
            
            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        
            # --- Timer going up ---
            # Calculate total seconds
            self.totalSeconds = frame_count // frame_rate
        
            # Divide by 60 to get total minutes
            minutes = self.totalSeconds // 60
        
            # Use modulus (remainder) to get seconds
            seconds = self.totalSeconds % 60
        
            # Use python string formatting to format in leading zeros
            # output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
            output_string = "Seconds: {0:01}".format(self.totalSeconds)
        
            # Blit to the screen
            text = basicfont.render(output_string, True, WHITE)
            screen.blit(text, [250, 250])
        
            # # --- Timer going down ---
            # # --- Timer going up ---
            # # Calculate total seconds
            # self.totalSeconds = start_time - (frame_count // frame_rate)
            # if self.totalSeconds < 0:
            #     self.totalSeconds = 0
        
   #        #   # Divide by 60 to get total minutes
            # minutes = self.totalSeconds // 60
        
   #        #   # Use modulus (remainder) to get seconds
            # seconds = self.totalSeconds % 60
        
   #        #   # Use python string formatting to format in leading zeros
            # output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
        
   #        #   # Blit to the screen
            # text = basicfont.render(output_string, True, WHITE)
        
   #        #   screen.blit(text, [250, 280])
        
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
            frame_count += 1
        
            # Limit frames per second
            clock.tick(frame_rate)
            
            pygame.display.flip()
        pygame.quit()
        print ('So long!')


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
