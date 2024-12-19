import pygame
import math
import constants

#character class
#x and y allow for positioning character on the screen
#also creating character dimensions
class Character():
    def __init__(self, x, y, animationList):
        self.flip = False
        self.animationList = animationList
        self.frame_index = 0
        self.action = 0 #0 is for idle, and 1 is for run
        self.update_time = pygame.time.get_ticks()
        self.running = False
        self.image = animationList[self.action][self.frame_index]
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    #allow for moving character
    #character is passed with x and y values and when
    #move is called, pixels are incremented based on key presses
    def move(self, dx, dy):
        self.running = False
        if dx != 0 or dy != 0:
            self.running = True
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

    #control the speed of animation to frame rate ratio
    def update(self):

        #check what action the dungeonPlayer is performing
        if self.running == True:
            self.updateAction(1)
        else:
            self.updateAction(0)


        animation_cooldown = 70
        #update image
        self.image = self.animationList[self.action][self.frame_index]
        #check if time has passed since last animation update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        #check if animation is completed
        if self.frame_index >= len(self.animationList[self.action]):
            self.frame_index = 0

    def updateAction(self, newAction):
        #check if new action is different to previous one
        if(newAction != self.action):
            self.action = newAction
            #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    #draw rectangle on the screen
    #this is to help draw the character on the screen
    #passing self object of character class and screen size as surface to draw method
    #flipped image to account for moving left and right and turning character
    def draw(self, surface):
        imgFlip = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(imgFlip, self.rect)
        pygame.draw.rect(surface, constants.RED, self.rect, 1)