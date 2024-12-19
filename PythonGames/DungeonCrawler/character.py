import pygame
import math
import constants

#character class
#x and y allow for positioning character on the screen
#also creating character dimensions
class Character():
    def __init__(self, x, y, animationList):
        self.flip = False
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animationList[self.frame_index]
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    #allow for moving character
    #character is passed with x and y values and when
    #move is called, pixels are incremented based on key presses
    def move(self, dx, dy):

        if dx < 0:
            self.flip = True
        if dx > 0:
            self.flip = False

        #help control diagonal movement speed
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)

        self.rect.x += dx
        self.rect.y += dy

    #draw rectangle on the screen
    #this is to help draw the character on the screen
    #passing self object of character class and screen size as surface to draw method
    #flipped image to account for moving left and right and turning character
    def draw(self, surface):
        imgFlip = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(imgFlip, self.rect)
        pygame.draw.rect(surface, constants.RED, self.rect, 1)