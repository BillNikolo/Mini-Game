import pygame
from pygame.locals import *
import random
# import os
# import pygame_assets as assets

# Constants
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
LINE1 = 85
LINE2 = 205
LINE3 = 315
BACKGROUND_SPEED = 150
CAR_VERT_SPEED = 180
CAR_HORIZ_SPEED = 200
STOP_SIGN_VIOLATION = 0
SCORE = 0
# Dimensions of the screen
WIDTH, HEIGHT = 600, 400

# Constant always true until we need to close/quit/exit the game
GAMEPLAY = True



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

    def update_background(self, dt):
        # Update the coordination of the st/end point
        self.backgroundX1 -= int(BACKGROUND_SPEED*dt)
        self.backgroundX2 -= int(BACKGROUND_SPEED*dt)
        if self.backgroundX1 <= -self.BackgroundRect.width:
            self.backgroundX1 = self.BackgroundRect.width
        if self.backgroundX2 <= -self.BackgroundRect.width:
            self.backgroundX2 = self.BackgroundRect.width

    def render_background(self):
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
        if self.rect.right < (WIDTH - 10):
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(int(CAR_HORIZ_SPEED*dt), 0)
        if self.rect.left > 10:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(int(-CAR_HORIZ_SPEED*dt), 0)

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
            self.rect.center = (2950, random.choice([LINE1, LINE2, LINE3]))


class NumTarget(pygame.sprite.Sprite):
    def __init__(self, png, x, y):
        # Call the Sprite Object in the def
        super(NumTarget, self).__init__()
        # Load the image from the file
        self.image = pygame.image.load(png)
        # Create the main rectangular of the Stop Sign
        self.rect = self.image.get_rect()
        # First position of the Stop Sign
        self.rect.center = (x, y)
        
    def update(self, dt):
        self.rect.move_ip(int(-BACKGROUND_SPEED*dt), 0)

        if self.rect.x < -50:
            self.rect.center = (2950, random.choice([LINE1, LINE2, LINE3]))
            

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Fill screen with white
screen.fill(WHITE)
# Title of the screen
pygame.display.set_caption("Racing Numbers")


# Create a clock for the game
clock = pygame.time.Clock()
FPS = 60

# Setting up Sprites

# Target Sprite

target_filenames = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png",
                    "8.png", "9.png"]
random.shuffle(target_filenames)
target_group = pygame.sprite.Group()
x = 700
count = 0
for filename in target_filenames:
    count += 1
    y = random.choice([LINE1, LINE2, LINE3])
    if count in [3, 5, 7, 9]:
        x += 400
    else:
        x += 200
    target = NumTarget(filename, x, y)
    target_group.add(target)


# Stop Sign Sprite

stop_sign_group = pygame.sprite.Group()
x = 700
for i in range(5):
    stop_sign = StopSign(x, random.choice([LINE1, LINE2, LINE3]))
    x += 600
    stop_sign_group.add(stop_sign)

background = Background()

# Car Sprite

car_sprite = pygame.sprite.Group()
car = Car()

all_sprites = pygame.sprite.Group()
all_sprites.add(car, stop_sign_group, target_group)
print(len(all_sprites))
print(len(stop_sign_group))
print(len(target_group))

collision_list = []
# Initializes the main loop of the game
while GAMEPLAY:
    # The time running
    dt = clock.tick(FPS)/700

    for event in pygame.event.get():
        # Events are the inputs of the player
        if event.type == pygame.QUIT:
            Gameplay = False

        if event.type in [pygame.KEYUP,pygame.KEYDOWN,pygame.K_RIGHT, pygame.K_LEFT]:
            car_sprite.update()

    # Update the background of the screen
    background.update_background(dt)
    background.render_background()

    # Draw sprites
    all_sprites.update(dt)
    all_sprites.draw(screen)

    # Update the whole screen

    # Detects Collision
    collision_list = pygame.sprite.spritecollide(car, stop_sign_group, True)
    if len(collision_list) > 0:
        if len(stop_sign_group) < 5:
            STOP_SIGN_VIOLATION += 1
            stop_sign = StopSign(collision_list[0].rect.x + 3000, random.choice([LINE1, LINE2, LINE3]))
            stop_sign_group.add(stop_sign)
            all_sprites.add(stop_sign)
            collision_list.remove(collision_list[0])
            if STOP_SIGN_VIOLATION == 3:
                GAMEPLAY = False

    pygame.display.update()

pygame.quit()