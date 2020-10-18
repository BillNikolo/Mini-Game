import pygame
import pygame_assets as assets

# Colors
Gray=(128,128,128)
White=(255,255,255)
pygame.init() # Initialize the game

Width, Height=600, 400
screen = pygame.display.set_mode((Width,Height)) # The dimensions of the window of the game
pygame.display.set_caption("Racing Numbers") # Create a caption for the game

Gameplay = True # Constant always true until we need to close/quit/exit the game

while Gameplay: #Initializes the main loop of the game
    screen.fill(Gray) # Fills the background with gray
    # Fills the road with road lines
    Roadline = pygame.Surface((75, 20))
    Roadline.fill(White)
    for i in range(1,8,2):
        for j in range(1,5):
            screen.blit(Roadline,(i*70,j*75))
    SideRoadLines = pygame.Surface((600, 15))
    SideRoadLines.fill(White)
    screen.blit(SideRoadLines, (0, 0))
    screen.blit(SideRoadLines, (0, 385))

    pygame.display.update() # Update the color of the screen
    for event in pygame.event.get():# Events are the inputs of the player
        if event.type == pygame.QUIT:
            Gameplay = False