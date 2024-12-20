import pygame
import constants
from character import Character
from weapon import Weapon

pygame.init()

#set game window screen, pass Screen_Width and height variable to it
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
#rename game title
pygame.display.set_caption("Dungeon Crawler")

#allow for sync to system clock for frame rate
systemClock = pygame.time.Clock()

#character movement variables definition
#set to false because the character isn't moving until buttons are pressed
movingLeft = False
movingRight = False
movingUp = False
movingDown = False

#scale image helper function
def scaleImage(image, scale):
    width = image.get_width()
    height = image.get_height()
    return pygame.transform.scale(image, (width * scale, height * scale))

#load weapon images
bow_image = pygame.image.load("assets/images/weapons/bow.png").convert_alpha()

#load character images
charactersAnimations = []
characterTypes = ["elf", "imp", "skeleton", "goblin", "muddy", "tiny_zombie", "big_demon"]


#pull image 0-3 and store in array and loop through them
#to give animation effect of character moving
animationTypes = ["idle", "run"]
for characterType in characterTypes:
    animationList = []
    for animation in animationTypes:
        #reset temp list of imgs
        tempList = []
        for i in range(4):
            img = pygame.image.load(f"assets/images/characters/{characterType}/{animation}/{i}.png").convert_alpha()
            img = scaleImage(img, constants.SCALE)
            tempList.append(img)
        animationList.append(tempList)
    charactersAnimations.append(animationList)

#player creation
dungeonPlayer = Character(100, 100, charactersAnimations, 0)

#create player's weapon
bow = Weapon(bow_image)

#loop to continue game
continueLoop = True
while(continueLoop):

    #game frame rate by using system clock method defined above
    systemClock.tick(constants.FPS)

    #allow Background color change
    #to account for character movement
    screen.fill(constants.BG)

    #calculate dungeonPlayer movement
    #update dx and dy coordinates if movement detection on keyboard
    #and move by 5 pixels, positive for right and down and negative for left and up
    dx = 0
    dy = 0
    if movingRight == True:
        dx = constants.SPEED
    if movingLeft == True:
        dx = -constants.SPEED
    if movingUp == True:
        dy = -constants.SPEED
    if movingDown == True:
        dy = constants.SPEED

    #move dungeonPlayer on screen
    dungeonPlayer.move(dx, dy)

    #update dungeonPlayer
    dungeonPlayer.update()
    bow.update(dungeonPlayer)

    # render dungeonPlayer on the screen
    dungeonPlayer.draw(screen)
    bow.draw(screen)

    #detect event/handler
    #look for events that have been picked up(such as clicking X to quit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #account for key presses on keyboard for movement of character/dungeonPlayer
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movingLeft = True
            if event.key == pygame.K_d:
                movingRight = True
            if event.key == pygame.K_w:
                movingUp = True
            if event.key == pygame.K_s:
                movingDown = True
        #account if key button is released, basically stopping movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movingLeft = False
            if event.key == pygame.K_d:
                movingRight = False
            if event.key == pygame.K_w:
                movingUp = False
            if event.key == pygame.K_s:
                movingDown = False



    #display method to pull draw methods to display everything
    #this displays the character on the screen
    pygame.display.update()

pygame.quit()