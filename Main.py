import pygame
import pygame_assets as assets

# Colors
Gray = (128, 128, 128)
White = (255, 255, 255)

pygame.init() # Initialize the game

Width, Height = 600, 400
screen = pygame.display.set_mode((Width, Height))  # The dimensions of the window of the game
pygame.display.set_caption("Racing Numbers")  # Create a caption for the game

# Background
background = pygame.image.load('Road.png')



Gameplay = True  # Constant always true until we need to close/quit/exit the game

while Gameplay:  # Initializes the main loop of the game
    screen.fill(Gray)  # Fills the background with gray
    # Background Image
    screen.blit(background, (0, 0))
    pygame.display.update()  # Update the color and background of the screen
    for event in pygame.event.get():  # Events are the inputs of the player
        if event.type == pygame.QUIT:
            Gameplay = False