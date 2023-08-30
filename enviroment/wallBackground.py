import pygame
from config import *


class wallBackground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.Vector2(x, y)
        self.image = pygame.image.load(walls['background'])
        self.rect = self.image.get_rect()
    
    def update(self) -> None:
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
    