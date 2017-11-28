'''
Planet.py

implements the Planet class
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import random
from GameObject import GameObject

screenWidth = 600
screenHeight = 800
planetSize = screenWidth//20
CHARCOAL = (28,28,28)
WHITE = (255,255,255)
BLACK = (0,0,0)

class Planet(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load('img/planet1.png').convert_alpha()
        # rows, cols = 4, 4
        # width, height = image.get_size()
        # cellWidth, cellHeight = width / cols, height / rows
        Planet.images = []
        Planet.images.append(image)
        # for i in range(rows):
        #     for j in range(cols):
        #         subImage = image.subsurface(
        #             (i * cellWidth, j * cellHeight, cellWidth, cellHeight))
        #         Planet.images.append(subImage)

    # minSize = 1
    # maxSize = 1
    # maxSpeed = 5

    def __init__(self, x, y):
        # if level is None:
            # level = random.randint(Planet.minSize, Planet.maxSize)
        # self.level = level
        # factor = self.level / Planet.maxSize
        image = random.choice(Planet.images)
        # w, h = image.get_size()
        # image = pygame.transform.scale(image, (int(w * factor), int(h * factor)))
        super(Planet, self).__init__(x, y, image)
        # self.angleSpeed = random.randint(-10, 10)
        # vx = random.randint(-Planet.maxSpeed, Planet.maxSpeed)
        # vy = random.randint(-Planet.maxSpeed, Planet.maxSpeed)
        # self.velocity = vx, vy
        
    # def update(self, screenWidth, screenHeight):
    #     self.angle += self.angleSpeed
    #     super(Planet, self).update(screenWidth, screenHeight)

    # def breakApart(self):
    #     if self.level == Planet.minSize:
    #         return []
    #     else:
    #         return [Planet(self.x, self.y, self.level - 1),
    #                 Planet(self.x, self.y, self.level - 1)]


def planetCoordsX(): #make a random planet and random size
    x = random.randrange(planetSize, screenWidth - planetSize)
    return x
    
def planetCoordsY():
    y = random.randrange(planetSize, screenHeight - planetSize)
    return y