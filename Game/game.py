import pygame
import Constants
from Player import *
import client
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants
SCREEN_WIDTH = Constants.SCREEN_WIDTH
SCREEN_HEIGHT = Constants.SCREEN_HEIGHT

pygame.init()

# Create a new screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Caption and icon
pygame.display.set_caption("Rock Paper Scissors")

# create players


running = True

# Main loop
while running:
    

    # Full the screen with black
    screen.fill((0, 0, 0))
    
    pygame.display.flip()

