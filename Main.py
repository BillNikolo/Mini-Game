import pygame
import pygame_assets as assets

# Colors
Gray = (128, 128, 128)
White = (255, 255, 255)


class Background():
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

        #Speed that the background moves
        self.backgroundSpeed = 4

    def updateBackground(self):
        # Update the coordination of the st/end point
        self.backgroundX1 -= self.backgroundSpeed
        self.backgroundX2 -= self.backgroundSpeed
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
        self.rect.center = (50, 80)


class StopSign(pygame.sprite.Sprite):
    def __init__(self):
        # Call the Sprite Object in the def
        super(StopSign, self).__init__()
        # Load the image from the file
        self.image = pygame.image.load("StopSign.png")
        # Create the main rectangular of the Stop Sign
        self.rect = self.image.get_rect()
        # First position of the Stop Sign
        self.rect.center = (500, 80)


NumTarget_list = pygame.sprite.Group()


class NumTarget(pygame.sprite.Sprite):
    def __init__(self):
        # Call the Sprite Object in the def
        super(NumTarget, self).__init__()
        # Load the image from the file
        self.image = pygame.image.load("1.png")
        # Create the main rectangular of the Stop Sign
        self.rect = self.image.get_rect()
        # First position of the Stop Sign
        self.rect.center = (500, 310)


# Initialize the game
pygame.init()
# Dimensions of the screen
Width, Height = 600, 400
screen = pygame.display.set_mode((Width, Height))
# Fill screen with white
screen.fill(White)
# Title of the screen
pygame.display.set_caption("Racing Numbers")

# Background
# background = pygame.image.load('Road.png')


# Constant always true until we need to close/quit/exit the game
Gameplay = True

# Create a clock for the game
clock = pygame.time.Clock()
FPS = 60

# Setting up Sprites
car = Car()
stopsign = StopSign()
background = Background()
numtarget = NumTarget()
NumTarget_list = pygame.sprite.Group()
car_list = pygame.sprite.Group()
NumTarget_list.add(numtarget)
car_list.add(car, stopsign)


while Gameplay:  # Initializes the main loop of the game
    # clock.tick(FPS)
    # Fills the background with gray
    # screen.fill(Gray)
    # Background Image
    # screen.blit(background, (0, 0))
    # Insert the Car Object into the screen
    NumTarget_list.draw(screen)
    car_list.draw(screen)
    # Update the color and background of the screen
    pygame.display.update()
    for event in pygame.event.get():  # Events are the inputs of the player
        if event.type == pygame.QUIT:
            Gameplay = False

    # Upadte the backgroun of the screen
    background.updateBackground()
    background.renderBackground()
    # Update the whole screen
    pygame.display.update()
    clock.tick(FPS)