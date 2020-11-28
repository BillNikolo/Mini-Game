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
CAR_VERT_SPEED = BACKGROUND_SPEED + 30
CAR_HORIZ_SPEED = BACKGROUND_SPEED + 50
STOP_VIOLATION = 0
NUMBER_VIOLATION = 0
SCORE = 0
check_list = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png",
                    "8.png", "9.png"]
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
        self.backgroundX1 -= BACKGROUND_SPEED*dt
        self.backgroundX2 -= BACKGROUND_SPEED*dt
        if self.backgroundX1 <= -self.BackgroundRect.width:
            self.backgroundX1 = self.BackgroundRect.width
        if self.backgroundX2 <= -self.BackgroundRect.width:
            self.backgroundX2 = self.BackgroundRect.width

    def render_background(self):
        # Draw the picture two times
        SCREEN.blit(self.background, (int(self.backgroundX1), int(self.backgroundY1)))
        SCREEN.blit(self.background, (int(self.backgroundX2), int(self.backgroundY2)))

class Scoreboard:
    def __init__(self, font, score, stop, mistake, boolean, color):
        self.sign1 = font.render(str("Score: "), boolean, color)
        SCREEN.blit(self.sign1, (75, 0))
        self.sign2 = font.render(str("STOP: "), boolean, color)
        SCREEN.blit(self.sign2, (230, 0))
        self.sign3 = font.render(str("MISTAKES: "), boolean, color)
        SCREEN.blit(self.sign3, (380, 0))
        self.score_sign = font.render(str(score), boolean, color)
        SCREEN.blit(self.score_sign, (160, 0))
        self.stop_vio_sign = font.render(str(stop), boolean, color)
        SCREEN.blit(self.stop_vio_sign, (310, 0))
        self.num_vio_sign = font.render(str(mistake), boolean, color)
        SCREEN.blit(self.num_vio_sign, (515, 0))



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
        self.x = x
        self.y = y

    def update(self, dt):        
        self.x -= BACKGROUND_SPEED*dt

        if self.x < -50:
            self.x = 2950
            self.y = random.choice([LINE1, LINE2, LINE3])

        self.rect.center = (int(self.x), int(self.y))

    def collision(self):
        self.x += 3000
        self.y = random.choice([LINE1, LINE2, LINE3])



class NumTarget(pygame.sprite.Sprite):
    def __init__(self, png, x, y):
        # Call the Sprite Object in the def
        super(NumTarget, self).__init__()
        # Load the image from the file
        self.png = png
        self.image = pygame.image.load(png)
        # Create the main rectangular of the Number
        self.rect = self.image.get_rect()
        # First position of the Stop Sign
        self.x = x
        self.y = y
        self.rect.center = (int(self.x), int(self.y))
        
    def update(self, dt):
        self.x -= BACKGROUND_SPEED*dt

        if self.x < -50:
            self.x = 2950
            self.y = random.choice([LINE1, LINE2, LINE3])

        self.rect.center = (int(self.x), int(self.y))

    def collision(self):
        self.x += 3000
        self.y = random.choice([LINE1, LINE2, LINE3])

    def png_return(self):
        return self.png

# Initialize the game


pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Title of the screen
pygame.display.set_caption("Racing Numbers")

# Initialize font of the gaming board
FONT = pygame.font.SysFont("Verdana", 20)

background = Background()

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

# Car Sprite

car_sprite = pygame.sprite.Group()
car = Car()

all_sprites = pygame.sprite.Group()
all_sprites.add(car, stop_sign_group, target_group)

# Initializes the main loop of the game
while GAMEPLAY:
    collision_stop = []
    collision_num = []
    # The time running
    dt = clock.tick(FPS)/1000

    for event in pygame.event.get():
        # Events are the inputs of the player
        if event.type == pygame.QUIT:
            GAMEPLAY = False


    # Update the background of the screen
    background.update_background(dt)
    background.render_background()

    Scoreboard(FONT, SCORE, STOP_VIOLATION, NUMBER_VIOLATION, True, WHITE)

    # Draw sprites
    all_sprites.update(dt)
    all_sprites.draw(SCREEN)


     # Detects Collision
    collision_stop = pygame.sprite.spritecollide(car, stop_sign_group, False)
    for stop_sign in collision_stop:
        STOP_VIOLATION += 1
        print('SSV', STOP_VIOLATION)
        stop_sign.collision()
        if STOP_VIOLATION == 3:
            GAMEPLAY = False

    collision_num = pygame.sprite.spritecollide(car, target_group, False)
    for target in collision_num:
        if check_list[SCORE] == target.png_return():
            SCORE += 1
            print('S', SCORE)
        else:
            NUMBER_VIOLATION += 1
            print('NV', NUMBER_VIOLATION)
            if NUMBER_VIOLATION == 3:
                GAMEPLAY = False

        target.collision()


    # Update the whole screen
    pygame.display.update()

pygame.quit()
