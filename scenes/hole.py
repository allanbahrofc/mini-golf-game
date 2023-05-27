import pygame
from pygame.sprite import _Group

class Hole(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('./res/ball_puck.png')
        self.pos = pygame.Vector2()