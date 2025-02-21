
import pygame


player_walk = [
    pygame.image.load("assets/walk_1.png"),
    pygame.image.load("assets/walk_2.png"),
    pygame.image.load("assets/walk_3.png")
]

player_jump = [
    pygame.image.load("assets/jump_1.png"),
    pygame.image.load("assets/jump_2.png")
]

player_crouch = [
    pygame.image.load("assets/crouch_1.png"),
    pygame.image.load("assets/crouch_2.png")
]


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        pass
