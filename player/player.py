
import pygame


player_walk = [
    pygame.image.load("assets/player_walk_1.png").convert(),
    pygame.image.load("assets/player_walk_2.png").convert(),
    pygame.image.load("assets/player_walk_3.png").convert()
]

player_jump = [
    pygame.image.load("assets/player_jump_1.png").convert(),
    pygame.image.load("assets/player_jump_2.png").convert()
]

player_crouch = [
    pygame.image.load("assets/player_crouch_1.png").convert(),
    pygame.image.load("assets/player_crouch_2.png").convert()
]


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        pass
