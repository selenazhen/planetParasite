'''
Planet.py

implements the Planet class
Citation: Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import random
# from GameObject import GameObject

screenWidth = 600
screenHeight = 800
planetSize = screenWidth//20
CHARCOAL = (28,28,28)
WHITE = (255,255,255)
BLACK = (0,0,0)

class Planet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((planetSize, planetSize), pygame.SRCALPHA)
        self.rect = self.image.get_rect() #Fetch the rectangle object that 
                                            #has the dimensions of the image.

    def moveLeft(self):
        self.x -= 10
        print (self.x,self.y)

    def moveRight(self):
        self.x += 10
        print (self.x,self.y)

    def moveUp(self):
        self.y -= 10
        print (self.x,self.y)

    def moveDown(self):
        self.y += 10
        print (self.x,self.y)

    def draw(self,screen,pCoordsX,pCoordsY): #call draw to show circles
        pygame.draw.circle(screen, WHITE,(pCoordsX,pCoordsY),
                            planetSize, 5) #testing circle


def planetCoordsX(): #make a random planet and random size
    
    x = random.randrange(planetSize, screenWidth - planetSize)
    return x
    
def planetCoordsY():
    y = random.randrange(planetSize, screenHeight - planetSize)
    return y