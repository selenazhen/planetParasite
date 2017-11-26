'''
pygamegame.py
created by Lukas Peraza
 for 15-112 F15 Pygame Optional Lecture, 11/11/15

use this code in your term project if you want
- CITE IT
- you can modify it to your liking
  - BUT STILL CITE IT

- you should remove the print calls from any function you aren't using
- you might want to move the pygame.display.flip() to your redrawAll function,
    in case you don't need to update the entire display every frame (then you
    should use pygame.display.update(Rect) instead)
'''
import pygame
import sys
from pygame.locals import *

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
        w,h,m = self.width,self.height,self.margin
        basicfont = pygame.font.Font("DINPro.otf", 20)
        textScore = basicfont.render('score: %d' % (self.score), True, WHITE)
        textScorerect = textScore.get_rect()
        textScorerect.centerx,textScorerect.centery = w//2, h-(m//2)
        textTitle = basicfont.render("planet parasite", True, WHITE)
        textTitlerect = textTitle.get_rect()
        textTitlerect.centerx,textTitlerect.centery = w//2, (m//2)
        
       
        pygame.draw.circle(screen, WHITE,(self.parasiteX,self.parasiteY),
                            m, 5) #testing circle
    
        pygame.draw.rect(screen, CHARCOAL,(0, 0, w, m)) #border top rect
        pygame.draw.rect(screen, CHARCOAL,(0, 0, m, h)) #border bottom rect
        pygame.draw.rect(screen, CHARCOAL,(w-m, 0, m, h)) #border top rect
        pygame.draw.rect(screen, CHARCOAL,(0, h-m, w, m)) #border top rect
        
        pygame.draw.rect(screen, WHITE,(m,m, w-(2*m),h-(2*m)), 2) #border
        screen.blit(textScore, textScorerect)
        screen.blit(textTitle, textTitlerect)

    def isKeyPressed(self, key):
        return self._keys.get(key, False)

    def __init__(self, width=600, height=800, fps=50, title="PLANET PARASITE"):
        self.width = width
        self.height = height
        self.margin= self.width//8
        self.fps = fps
        self.title = title
        self.parasiteX = self.width//2
        self.parasiteY = self.height//2
        self.speed = 25
        self.score = 0
        pygame.init()

    def run(self):
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
            
            pygame.display.flip()
        pygame.quit()
        print ('So long!')


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
