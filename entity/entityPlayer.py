from pygame.locals import *
from config import *
import pygame


class entityPlayer(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.pos = pygame.Vector2(self.x, self.y)
        self.image = pygame.image.load(sprites['ballOneSprite'])
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.velocity = 1.5
        self.direction = None
        self.gameOver = False

    def movePlayer(self):
        keys = pygame.key.get_pressed()

        if keys[K_UP] or keys[K_w]:
            self.direction = 'UP'
        elif keys[K_DOWN] or keys[K_s]:
            self.direction = 'DOWN'
        elif keys[K_LEFT] or keys[K_a]:
            self.direction = 'LEFT'
        elif keys[K_RIGHT]  or keys[K_d]:
            self.direction = 'RIGHT'

        if self.direction == 'UP':
            self.pos.y -= 1*self.velocity
        elif self.direction == 'DOWN':
            self.pos.y += 1*self.velocity
        elif self.direction == 'LEFT':
            self.pos.x -= 1*self.velocity
        elif self.direction == 'RIGHT':
            self.pos.x += 1*self.velocity
        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def collisionBorders(self):
        if self.pos.x > window['width'] or self.pos.x < 0 or self.pos.y > window['height'] or self.pos.y < 0:
            self.killPlayer()

    def update(self) -> None:
        self.movePlayer()
        self.collisionBorders()

    def killPlayer(self):
        self.gameOver = True
        self.kill()
