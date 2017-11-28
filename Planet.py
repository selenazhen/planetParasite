# '''
# Planet.py
# 
# implements the Planet class
# Citation: Lukas Peraza, 2015 for 15-112 Pygame Lecture
# '''
# import pygame
# import random
# from GameObject import GameObject
# 
screenWidth = 600
screenHeight = 800
planetSize = screenWidth//20
CHARCOAL = (28,28,28)
WHITE = (255,255,255)
BLACK = (0,0,0)
# 
# 
# class Planet(GameObject):
#     @staticmethod
#     def init():
#         image = pygame.image.load('img/planet1.png').convert_alpha()
#         Planet.images = []
#         Planet.images.append(image)
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# 
# 

'''
Planet.py

implements the Planet class
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import random
from GameObject import GameObject


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

    minSize = 2
    maxSize = 6
    maxSpeed = 5

    def __init__(self, x, y, level=None):
        if level is None:
            level = random.randint(Planet.minSize, Planet.maxSize)
        self.level = level
        factor = self.level / Planet.maxSize
        image = random.choice(Planet.images)
        w, h = image.get_size()
        image = pygame.transform.scale(image, (int(w * factor), int(h * factor)))
        super(Planet, self).__init__(x, y, image, w / 2 * factor)
        self.angleSpeed = random.randint(-10, 10)
        vx = random.randint(-Planet.maxSpeed, Planet.maxSpeed)
        vy = random.randint(-Planet.maxSpeed, Planet.maxSpeed)
        self.velocity = vx, vy

    def update(self,left,right,up,down):
        self.x += left
    # def update(self, screenWidth, screenHeight):
    #     self.angle += self.angleSpeed
    #     super(Planet, self).update(screenWidth, screenHeight)

    # def breakApart(self):
    #     if self.level == Planet.minSize:
    #         return []
    #     else:
    #         return [Planet(self.x, self.y, self.level - 1),
    #                 Planet(self.x, self.y, self.level - 1)]


# class Planet(pygame.sprite.Sprite):
#     def __init__(self,x,y):
#         # Call the parent class (Sprite) constructor
#         super().__init__()
#         self.x = x
#         self.y = y
#         self.image = pygame.Surface((planetSize, planetSize), pygame.SRCALPHA)
#         self.rect = self.image.get_rect() #Fetch the rectangle object that 
#                                             #has the dimensions of the image.
#         pygame.draw.circle(self.image, WHITE,(x,y),
#                             planetSize, 2) #testing circle
# 
#     def moveLeft(self):
#         self.x -= 10
#         print (self.x,self.y)
# 
#     def moveRight(self):
#         self.x += 10
#         print (self.x,self.y)
# 
#     def moveUp(self):
#         self.y -= 10
#         print (self.x,self.y)
# 
#     def moveDown(self):
#         self.y += 10
#         print (self.x,self.y)
# 
#     def draw(self,screen,pCoordsX,pCoordsY): #call draw to show circles
#         pygame.draw.circle(screen, WHITE,(pCoordsX,pCoordsY),
#                             planetSize, 2) #testing circle


# class Planet(pygame.sprite.Sprite):
#     def __init__(self,coords):
#         self.x = coords[0]
#         self.y = coords[1]
#         pygame.sprite.Sprite.__init__(self)
#         self.image=pygame.Surface((50,50))
#         self.rect=self.image.get_rect()
#         self.image.fill((255,255,255))
#         pygame.draw.circle(self.image,(0,0,0),(25,25),25,0)
#         
#         self.rect.center=(self.x,self.y)
#         
#     def moveLeft(self):
#         self.x -= 10
#         print (self.x,self.y)
# 
#     def moveRight(self):
#         self.x += 10
#         print (self.x,self.y)
# 
#     def moveUp(self):
#         self.y -= 10
#         print (self.x,self.y)
# 
#     def moveDown(self):
#         self.y += 10
#         print (self.x,self.y)

def planetCoordsX(): #make a random planet and random size
    x = random.randrange(planetSize, screenWidth - planetSize)
    return x
    
def planetCoordsY():
    y = random.randrange(planetSize, screenHeight - planetSize)
    return y
# 
# def planetCoords():
#     x = random.randrange(planetSize, screenWidth - planetSize)
#     y = random.randrange(planetSize, screenHeight - planetSize)
#     return (x,y)
    