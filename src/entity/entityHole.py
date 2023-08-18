from config import *
import random
import pygame


class entityHole(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(0, window['width']-25)
        self.y = random.randint(0, window['height']-25)
        self.pos = pygame.Vector2(self.x, self.y)
        self.image = pygame.image.load(sprites['holeOneSprite'])
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def respawnHole(self):
        # Reset the hole position and image to a new one
        self.pos.x = random.randint(0, window['width']-25)
        self.pos.y = random.randint(0, window['height']-25)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def delete(self):
        self.kill()
