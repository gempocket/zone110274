#COPILOT GENERATED PYGAME BASIC FILE
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 55

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.DOUBLEBUF)
pygame.display.set_caption("Pygame Window")

# Clock object to control the frame rate
clock = pygame.time.Clock()


# Groups
background = pygame.sprite.Group()
middleground = pygame.sprite.Group()
foreground = pygame.sprite.Group()


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with a black color
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
