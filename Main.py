import pygame, sys
from pygame.locals import *
import random, time
import os
import pygame_assets as assets

# Colors
Gray = (128, 128, 128)
White = (255, 255, 255)

#line_list = [(700,85),(700,180),(700,230)]
LINE1 = (700,85)
LINE2 = (700,180)
LINE3 = (700,235)
BACKGROUND_SPEED = 150
CAR_VERT_SPEED = 180


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

    def updateBackground(self, dt):
        # Update the coordination of the st/end point
        self.backgroundX1 -= int(BACKGROUND_SPEED*dt)
        self.backgroundX2 -= int(BACKGROUND_SPEED*dt)
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

    def update(self, dt):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 30:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, int(-CAR_VERT_SPEED*dt))
        if self.rect.bottom < 370:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, int(CAR_VERT_SPEED*dt))


class StopSign(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Call the Sprite Object in the def
        super(StopSign, self).__init__()
        # Load the image from the file
        self.image = pygame.image.load("StopSign.png")
        # Create the main rectangular of the Stop Sign
        self.rect = self.image.get_rect()
        # First position of the Stop Sign
        self.rect.center = (x, y)
        
    def update(self, dt):
        self.rect.move_ip(int(-BACKGROUND_SPEED*dt), 0)

        if self.rect.x < -50:
            self.rect.move_ip(random.choice([LINE1, LINE2, LINE3]))


class NumTarget(pygame.sprite.Sprite):
    def __init__(self, png, x, y):
        # Call the Sprite Object in the def
        super(NumTarget, self ).__init__()
        # Load the image from the file
        self.image = pygame.image.load(png)
        # Create the main rectangular of the Stop Sign
        self.rect = self.image.get_rect()
        # First position of the Stop Sign
        self.rect.center = (x, y)
        
    def update(self, dt):
        self.rect.move_ip(int(-BACKGROUND_SPEED*dt), 0)

        if self.rect.x < -50:
            self.rect.move_ip(int(600 + random.random()*300), int(random.random() * 200))
            

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
target_filenames = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png",
                    "8.png", "9.png"]
random.shuffle(target_filenames)
target_group = pygame.sprite.Group()
x = 700
for filename in target_filenames:
    y = int(random.random() * 3 * (Height / 3))
    target = NumTarget(filename, x, y)
    x += int(300 + random.random() * 600)
    target_group.add(target)

car = Car()
stop_sign = StopSign(500, 85)
background = Background()

car_sprite = pygame.sprite.Group()
car = Car()

all_sprites = pygame.sprite.Group()
all_sprites.add(car)
all_sprites.add(stop_sign)
all_sprites.add(target_group)

# Initializes the main loop of the game
while Gameplay:
    # The time running
    dt = clock.tick(FPS)/700

    for event in pygame.event.get():
        # Events are the inputs of the player
        if event.type == pygame.QUIT:
            Gameplay = False

        if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
            car_sprite.update()

    # Update the background of the screen
    background.updateBackground(dt)
    background.renderBackground()
    # Draw sprites
    all_sprites.update(dt)
    all_sprites.draw(screen)
    # Update the whole screen
    pygame.display.update()

pygame.quit()