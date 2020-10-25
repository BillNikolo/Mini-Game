import pygame
import pygame_assets as assets

# Colors
Gray = (128, 128, 128)
White = (255, 255, 255)


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


# Initialize the game
pygame.init()
# Dimensions of the screen
Width, Height = 600, 400
screen = pygame.display.set_mode((Width, Height))
# Title of the screen
pygame.display.set_caption("Racing Numbers")

# Background
background = pygame.image.load('Road.png')


# Constant always true until we need to close/quit/exit the game
Gameplay = True
clock = pygame.time.Clock()
FPS = 60
Car = Car()
car_list = pygame.sprite.Group()
car_list.add(Car)
while Gameplay:  # Initializes the main loop of the game
    clock.tick(FPS)
    # Fills the background with gray
    screen.fill(Gray)
    # Background Image
    screen.blit(background, (0, 0))
    # Insert the Car Object into the screen
    car_list.draw(screen)
    # Update the color and background of the screen
    pygame.display.update()
    for event in pygame.event.get():  # Events are the inputs of the player
        if event.type == pygame.QUIT:
            Gameplay = False