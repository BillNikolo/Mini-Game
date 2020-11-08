import pygame, sys
from pygame.locals import *
import random, time
import os
import bpy
import pygame_assets as assets

# Colors
Gray = (128, 128, 128)
White = (255, 255, 255)

SPEED = 5


class Background:
    def __init__(self):
        # Create a rectangle of Road picture(600x400)
        self.background = pygame.image.load('Road.png')
        self.BackgroundRect = self.background.get_rect()

        # Set coordination for starting point
        self.backgroundY1 = 0
        self.backgroundX1 = 0

        # Set coordination for the point at the end
        self.backgroundY2 = 0
        self.backgroundX2 = self.BackgroundRect.width

        # Speed that the background moves
        self.backgroundSpeed = 4

    def updateBackground(self, time):
        # Update the coordination of the st/end point
        self.backgroundX1 -= self.backgroundSpeed/time
        self.backgroundX2 -= self.backgroundSpeed/time
        if self.backgroundX1 <= -self.BackgroundRect.width:
            self.backgroundX1 = self.BackgroundRect.width
        if self.backgroundX2 <= -self.BackgroundRect.width:
            self.backgroundX2 = self.BackgroundRect.width

    def renderBackground(self):
        # Draw the picture two times
        screen.blit(self.background, (self.backgroundX1, self.backgroundY1))
        screen.blit(self.background, (self.backgroundX2, self.backgroundY2))


class Car(pygame.sprite.Sprite):
    def __init__(self):
        # Call the Sprite Object in the def
        super(Car, self).__init__()
        # Load the image from the file
        self.image = pygame.image.load("Car.png")
        # Create the main rectangular of the Car
        self.rect = self.image.get_rect()
        # First position of the Car
        self.rect.center = (50, 85)

    def drive(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 30:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < 370:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)


class StopSign(pygame.sprite.Sprite):
    def __init__(self):
        # Call the Sprite Object in the def
        super(StopSign, self).__init__()
        # Load the image from the file
        self.image = pygame.image.load("StopSign.png")
        # Create the main rectangular of the Stop Sign
        self.rect = self.image.get_rect()
        # First position of the Stop Sign
        self.rect.center = (500, 85)


class NumTarget(pygame.sprite.Sprite):
    def __init__(self, png):
        # Call the Sprite Object in the def
        super(NumTarget, self ).__init__()
        # Load the image from the file
        self.image = pygame.image.load(png)
        # Create the main rectangular of the Stop Sign
        self.rect = self.image.get_rect()
        # First position of the Stop Sign
        # self.rect.center = (500, 320)


# Initialize the game
pygame.init()
# Dimensions of the screen
Width, Height = 600, 400
screen = pygame.display.set_mode((Width, Height))
# Fill screen with white
screen.fill(White)
# Title of the screen
pygame.display.set_caption("Racing Numbers")


# Constant always true until we need to close/quit/exit the game
Gameplay = True

# Create a clock for the game
clock = pygame.time.Clock()
FPS = 60

# Setting up Sprites
target_list = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png",
               "8.png", "9.png"]
NumTarget_list = pygame.sprite.Group()
for i in range(len(target_list)):
    num_target = NumTarget(target_list[i])
    NumTarget_list.add(num_target)

car = Car()
stop_sign = StopSign()
background = Background()
CAR = pygame.sprite.Group()
CAR.add(car)#, stop_sign)

#Adding a new User event
NEW_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(NEW_EVENT, 1000)

# Initializes the main loop of the game
while Gameplay:
    # The time running
    clock.tick(FPS)
    # dt of the last two loops in milliseconds
    dt = clock.get_time()/20

    for event in pygame.event.get():
        # Events are the inputs of the player
        for event in pygame.event.get():
            if event.type == NEW_EVENT:
                SPEED += 0.5
        if event.type == pygame.QUIT:
            Gameplay = False

    # Update the background of the screen
    background.updateBackground(dt)
    background.renderBackground()
    # Insert the Car Object into the screen
    NumTarget_list.draw(screen)
    CAR.draw(screen)
    for entity in CAR:
        entity.drive()
    # Update the whole screen
    pygame.display.update()
