from pygame.locals import *
from scene_configuration import *
import pygame

class entityPlayer(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = pygame.Vector2(self.x, self.y)
        self.sprite = pygame.image.load(sprites['ballOneSprite'])
        self.rect = pygame.Surface.get_rect(self.sprite)
        self.velocity = 1.2
        self.direction = None

    def move(self):
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

    def checkCollision(self, collider):
        if self.rect.colliderect(collider):
            print('collider')

    def update(self):
        self.move()

    def delete(self):
        self.kill()
