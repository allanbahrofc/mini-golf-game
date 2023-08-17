from typing import Any
from pygame.locals import *
from config import *
import pygame


class entityPlayer(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 150
        self.y = 225
        self.pos = pygame.Vector2(self.x, self.y)
        self.image = pygame.image.load(sprites['ballOneSprite'])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = 1.5
        self.direction = None

    def movePlayer(self):
        keys = pygame.key.get_pressed()

        if keys[K_UP]:
            self.direction = 'UP'
        elif keys[K_DOWN]:
            self.direction = 'DOWN'
        elif keys[K_LEFT]:
            self.direction = 'LEFT'
        elif keys[K_RIGHT]:
            self.direction = 'RIGHT'

        if self.direction == 'UP':
            self.pos.y -= 1*self.velocity
        elif self.direction == 'DOWN':
            self.pos.y += 1*self.velocity
        elif self.direction == 'LEFT':
            self.pos.x -= 1*self.velocity
        elif self.direction == 'RIGHT':
            self.pos.x += 1*self.velocity
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.movePlayer()
        return super().update(*args, **kwargs)
    
    def killPlayer(self):
        self.kill()
