import pygame
from pygamegame import PygameGame
from Planet import Planet, planetCoords
import random


'''
Game.py

Actually implements the game
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''

CHARCOAL = (31,31,31)
WHITE = (255,255,255)
BLACK = (0,0,0)




class Game(PygameGame):
    def init(self):
        pass
    
    def __init__(self, w,h):
        super().__init__()
        self.timePassed = pygame.time.get_ticks()
        

    def keyPressed(self, code, mod):
        pass

    def timerFired(self, dt):
        # self.timePassed += dt
        # # print (self.timePassed)
        # if self.timePassed %10 == 0:
        #     print ('hello', self.timePassed)
        # print (self.timePassed)
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

Game(600, 800).run()