import pygame
from pygame.locals import *
import random
import time
# import os
# import pygame_assets as assets

# Constants
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 250, 205)
BLUE = (100, 149, 237)
RED = (255, 0, 0)
LINE1 = 85
LINE2 = 205
LINE3 = 315
BACKGROUND_SPEED = 150
CAR_VERT_SPEED = BACKGROUND_SPEED + 30
CAR_HORIZ_SPEED = BACKGROUND_SPEED + 50
SCORE = 0
LIVES = 5
CHECK = 0
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
    def __init__(self, score, lives, boolean, color):
        self.score = score
        self.lives = lives
        self.font = pygame.font.SysFont("Verdana", 20)
        self.boolean = boolean
        self.color = color
        self.sign1 = self.font.render(str("SCORE: "), self.boolean, self.color)
        self.sign2 = self.font.render(str("LIVES: "), self.boolean, self.color)

    def update_lives(self):
        global GAMEPLAY
        self.lives -= 1
        self.score -= 50

    def update_score(self):
        global CHECK, GAMEPLAY
        self.score += 100

    def draw_scoreboard(self):
        self.score_sign = self.font.render(str(self.score), self.boolean, self.color)
        self.lives_sign = self.font.render(str(self.lives), self.boolean, self.color)
        SCREEN.blit(self.sign1, (175, 0))
        SCREEN.blit(self.sign2, (330, 0))
        SCREEN.blit(self.score_sign, (260, 0))
        SCREEN.blit(self.lives_sign, (410, 0))

    def win_or_lose(self):
        global CHECK, GAMEPLAY
        self.wolfont = pygame.font.SysFont("Verdana", 50)
        if CHECK == 10:
            SCREEN.fill(YELLOW)
            self.signw1 = self.wolfont.render(str("VICTORY!!"), True, BLUE)
            self.signw2 = self.wolfont.render(str(self.score), True, BLUE)
            SCREEN.blit(self.signw1, (240, 130))
            SCREEN.blit(self.signw2, (250, 180))
            pygame.display.update()
            time.sleep(5)
            GAMEPLAY = False
        elif self.lives == 0:
            SCREEN.fill(RED)
            self.signl1 = self.wolfont.render(str("LOST"), True, YELLOW)
            self.signl2 = self.wolfont.render(str(self.score), True, YELLOW)
            SCREEN.blit(self.signl1, (210, 130))
            SCREEN.blit(self.signl2, (240, 180))
            pygame.display.update()
            time.sleep(5)
            GAMEPLAY = False


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
    def __init__(self, n, x, y):
        # Call the Sprite Object in the def
        super(NumTarget, self).__init__()
        # Load the image from the file
        self.png = str(n)+'.png'
        self.image = pygame.image.load(self.png)
        # Create the main rectangular of the Number
        self.rect = self.image.get_rect()
        # First position of the Stop Sign
        self.x = x
        self.y = y
        self.num = n
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

    def get_num(self):
        return self.num

# Initialize the game


pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Title of the screen
pygame.display.set_caption("Racing Numbers")

background = Background()
scoreboard = Scoreboard(SCORE, LIVES, True, WHITE)

# Create a clock for the game
clock = pygame.time.Clock()
FPS = 60

# Setting up Sprites

# Target Sprite

target_file_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(target_file_number)
target_group = pygame.sprite.Group()
x = 700
count = 0
for file_number in target_file_number:
    count += 1
    y = random.choice([LINE1, LINE2, LINE3])
    if count in [3, 5, 7, 9]:
        x += 400
    else:
        x += 200
    target = NumTarget(file_number, x, y)
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

    scoreboard.draw_scoreboard()

    # Draw sprites
    all_sprites.update(dt)
    all_sprites.draw(SCREEN)

    # Detects Collision
    collision_stop = pygame.sprite.spritecollide(car, stop_sign_group, False)
    for stop_sign in collision_stop:
        stop_sign.collision()
        scoreboard.update_lives()

    collision_num = pygame.sprite.spritecollide(car, target_group, False)
    for target in collision_num:
        if target.get_num() == CHECK:
            scoreboard.update_score()
            CHECK += 1
        else:
            scoreboard.update_lives()

        target.collision()

    scoreboard.win_or_lose()
    # Update the whole screen
    pygame.display.update()

pygame.quit()
