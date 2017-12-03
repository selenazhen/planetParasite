"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/qbEEcQXw8aw
"""
 
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
 
    def update(self):
        """ Called each frame. """
 
        # Move block down one pixel
        self.rect.y += 1
 
        # If block is too far down, reset to top of screen.
        if self.rect.y > 410:
            self.reset_pos()
 
 
class Player(Block):
    """ The player class derives from Block, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    block = Block(BLACK, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = Player(RED, 20, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Calls update() method on every sprite in the list
    all_sprites_list.update()
 
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
 
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)
 
        # Reset block to the top of the screen to fall again.
        block.reset_pos()
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Limit to 20 frames per second
    clock.tick(20)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()



#! /usr/bin/env python
############################################################################
# File name : detectSpriteCollsion.py
# Purpose : Demostarting The Killing of Sprite On Collision
# Usages : Logic can be used in real time games
# Start date : 04/01/2012
# End date : 04/01/2012
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# How To Run: python detectSpriteCollision.py 
############################################################################
  
# import pygame
# from pygame.locals import *
# import random
#   
# screen=pygame.display.set_mode((640,480),0,32)
# pygame.display.set_caption("Collision Detection")
#   
#   
# #creating the boxes
# class Boxes(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image=pygame.Surface((50,50))
#         self.rect=self.image.get_rect()
#         self.image.fill((255,255,255))
#         pygame.draw.circle(self.image,(0,0,0),(25,25),25,0)
#         
#         self.rect.center=(100,100)
#   
# #creating circle
# class Circle(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image=pygame.Surface((50,50))
#         self.image.fill((0,255,0))
#         pygame.draw.circle(self.image,(255,0,0),(25,25),25,0)
#         self.rect=self.image.get_rect()
#     def update(self):
#         self.rect.center=pygame.mouse.get_pos()
#   
#   
# def main():
#     background=pygame.Surface(screen.get_size())
#     background=background.convert()
#     background.fill((255,255,255))
#     screen.blit(background,(0,0))
#   
#     boxes=[]
#     for i in range(0,10):
#         boxes.append(Boxes())
#   
#     circle=Circle()
#     allSprites=pygame.sprite.Group(boxes)
#     circleSprite=pygame.sprite.Group(circle)
#     while 1:
#         for i in pygame.event.get():
#             if i.type==QUIT:
#                 exit()
#   
#   
#         #checking the collision.check 'pydoc pygame.sprite.spritecollide' for mode details. True is used for sprite killing. It doesn't kill the sprite in actual.It is still present in the computer memory though.It has just removed it from the group so that no further display of that sprite is possible.
#         if pygame.sprite.spritecollide(circle,allSprites,True):
#             print ("collision")
#   
#         #following the CUD method
#         allSprites.clear(screen,background)
#         circleSprite.clear(screen,background)
#         allSprites.update()
#         circleSprite.update()
#         allSprites.draw(screen)
#         circleSprite.draw(screen)
#         pygame.display.flip()
#   
#   
# if __name__=='__main__':
#     main()
#   
# """You can also check the collision about the rect attributes. There are many ways to do that.Example:
# 1.circle.rect.colliderect(box1) will check the collision between the circle and box1 collision
# 2. pygame.sprite.collide_rect(sprite1,sprite2) willl also do the same """
#   


####
# import pygame
# import sys
# from pygame.locals import *
# 
# class StickMan(pygame.sprite.Sprite):
# 
#     # We’ll just accept the x-position here
#     def __init__(self, xPosition, yPosition):
# 
#         pygame.sprite.Sprite.__init__(self)
#         self.old = (0, 0, 0, 0)
#         self.image = pygame.image.load('img/planet1.png').convert_alpha()
#         self.rect = self.image.get_rect()
#         self.rect.x = xPosition
#         self.rect.y = yPosition
# 
#     # The x-position remains the same
#     def update(self, xPosition):
# 
#         self.old = self.rect
#         self.rect = self.rect.move([xPosition - self.rect.x, 0])
# 
# # Define a function to erase old sprite positions
# # This will be used later
# def eraseSprite(screen, rect):
#     screen.blit(blank, rect)
# 
# pygame.init()
# screen = pygame.display.set_mode((256, 256))
# # pygame.display.set_caption(‘Sprite Groups’)
# screen.fill((255, 255, 255))
# 
# # Create the three stick men
# stick1 = StickMan(0,25)
# stick2 = StickMan(0,75)
# stick3 = StickMan(0,125)
# 
# # Create a group and add the sprites
# stickGroup = pygame.sprite.Group()
# stickGroup.add((stick1, stick2, stick3))
# 
# # Add a variable for the direction, y-position and height of the
# # sprite we are dealing with
# stickGroup.direction = 'up'
# stickGroup.y = screen.get_rect().centery
# stickGroup.x = screen.get_rect().centerx
# stickGroup.height = stick1.rect.height
# 
# # Create a blank piece of background
# blank = pygame.Surface((stick1.rect.width, stick1.rect.height))
# blank.fill((255, 255, 255))
# 
# pygame.display.update()
# 
# # Create an event that will appear ever 100 milliseconds
# # This will be used to update the screen
# pygame.time.set_timer(pygame.USEREVENT + 1, 100)
# 
# while True:
# 
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         if (event.type == pygame.KEYDOWN) and (event.key == K_UP):
#             print ('left')
#             # stickGroup.rect.x = stickGroup.rect.x - 10
#             stickGroup.y = stickGroup.y + 10
# 
#         # Check for our update event
#         if event.type == pygame.USEREVENT + 1:
# 
#         # Update the y-position
#             if stickGroup.direction == 'up':
#                 stickGroup.y = stickGroup.y - 10
#             else:
#                 stickGroup.y = stickGroup.y + 10
# 
#         # Check if we have gone off the screen
#         # If we have, fix it
#         if stickGroup.direction == 'up' and stickGroup.y <= 0:
#             stickGroup.direction = 'down'
#         elif stickGroup.direction == 'down' and stickGroup.y >= (screen.get_rect().height - stickGroup.height):
#             stickGroup.direction = 'up'
#             stickGroup.y = screen.get_rect().height - stickGroup.height
# 
#         # Clear the old sprites
#         # Notice that we pass our eraseSprite function
#         # This will be called, and the screen and old position will be passed
#         stickGroup.clear(screen, eraseSprite)
# 
#         # Update the sprites
#         stickGroup.update(stickGroup.y)
# 
#         # Blit the sprites
#         stickGroup.draw(screen)
# 
#         # Create a list to store the updated rectangles
#         updateRects = []
# 
#         # Get the updated rectangles
#         for man in stickGroup:
#             updateRects.append(man.old)
#             updateRects.append(man.rect)
#         pygame.display.update(updateRects)

##### WORKING: MOVING PLANETS WITH ARROW KEYS BELOW
# ''' pygame_sprite_keys1.py
# move a sprite rect with the arrow keys
# see also ...
# http://www.pygame.org/docs/ref/sprite.html
# http://www.pygame.org/docs/ref/time.html
# '''
# 
# import pygame as pygame
# import sys
# from pygame.locals import *
# import random
# 
# speed = 5
# 
# pygame.init()
# width = 640
# height = 480
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("move with arrow keys (escape key to exit)")
# 
# # color (r, g, b) tuple, values 0 to 255
# white = (255, 255, 255)
# background = pygame.Surface(screen.get_size())
# background.fill(white)
# 
# class Planet(pygame.sprite.Sprite):
# 
#     def __init__(self, xPosition, yPosition):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load('img/planet1.png').convert_alpha()
#         self.rect = self.image.get_rect()
#         self.rect.centerx = xPosition
#         self.rect.centery = yPosition
#     def move(self, xMove,yMove):
#         self.rect.centerx = self.rect.centerx + xMove
#         self.rect.centery = self.rect.centery + yMove
# 
# planet1 = Planet(random.randrange(0,width),random.randrange(0,height))
# planet2 = Planet(random.randrange(0,width),random.randrange(0,height))
# planetGroup = pygame.sprite.Group()
# planetGroup.add((planet1, planet2))
# 
# clock = pygame.time.Clock()
# while 1:
#     # limit runtime speed to 30 frames/second
#     clock.tick(30)
#     keyinput = pygame.key.get_pressed()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             raise SystemExit
#         if (event.type == pygame.KEYDOWN) and (event.key == K_LEFT):
#             for planet in planetGroup:
#                 planet.move(-speed,0)
#         if (event.type == pygame.KEYDOWN) and (event.key == K_RIGHT):
#             for planet in planetGroup:
#                 planet.move(speed,0)
#         if (event.type == pygame.KEYDOWN) and (event.key == K_UP):
#             for planet in planetGroup:
#                 planet.move(0,-speed)
#         if (event.type == pygame.KEYDOWN) and (event.key == K_DOWN):
#             for planet in planetGroup:
#                 planet.move(0,speed)
#         if (event.type == pygame.KEYDOWN) and (event.key == K_ESCAPE):
#             playing = False
#     screen.blit(background, (0, 0))
#     planetGroup.draw(screen)
#     # update display
#     pygame.display.flip()