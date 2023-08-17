from config import *
import random
import pygame


class entityHole(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(0, window['width']-50)
        self.y = random.randint(0, window['height']-50)
        self.pos = pygame.Vector2(self.x, self.y)
        self.image = pygame.image.load(sprites['holeOneSprite'])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
  
    def delete(self):
        self.kill()
