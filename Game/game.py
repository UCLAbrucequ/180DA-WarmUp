import pygame
import Constants
import rps_mqtt_client as client
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

# create two clients
player1 = client.create_client()

running = True

# Main loop
while running:
    
    screen.fill((0, 0, 0))
    # Full the screen with black
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    
    pygame.display.flip()

