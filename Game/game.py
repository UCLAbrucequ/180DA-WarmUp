import pygame
import Constants
from Player import *
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
pygame.display.set_caption("Fruit Fight")


player = Player()

running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.type == QUIT:
                running = False
    # Get all the keys currently pressed
    pressed_key = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_key)

    # Full the screen with black
    screen.fill((0, 0, 0))
    screen.blit(player.surf, player.rect)
    pygame.display.flip()

