from config import *
import random
import pygame


class entityHole(pygame.sprite.Sprite):

    def __init__(self):
        self.x = random.randint(0, window['width']-50)
        self.y = random.randint(0, window['height']-50)
        self.pos = pygame.Vector2(self.x, self.y)
        self.sprite = pygame.image.load(sprites['holeOneSprite'])
        self.rect = self.sprite.get_rect()

    def checkCollision(self, collider):
        if self.rect.center == collider.rect.center:
            print('collide objects affected')
        else:
            print('not collide')
    def delete(self):
        self.kill()
