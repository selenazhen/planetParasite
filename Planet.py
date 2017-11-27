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
    # def init():
        # image = None
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        # self.image = image
        image = pygame.Surface((planetSize, planetSize), pygame.SRCALPHA)
        pygame.draw.circle(image, WHITE,(self.x,self.y),
                            planetSize, 5) #testing circle

def planetCoords(): #make a random planet and random size
    # planet = Planet(0,0) #assigning class
    # planet = (x,y)
    
    # planet.x = random.randrange(planetSize, screenWidth - planetSize)
    # planet.y = random.randrange(planetSize, screenHeight - planetSize)
    
    x = random.randrange(planetSize, screenWidth - planetSize)
    y = random.randrange(planetSize, screenHeight - planetSize)
 
    # print ((x,y))
    return ([x,y])