from entity.entityPlayer import entityPlayer
from pygame.locals import *
from scene_configuration import config, colors, sprites, walls
import random
import pygame
pygame.init()
title = pygame.display.set_caption('Mini Golf')
screen = pygame.display.set_mode([config['width'], config['height']])

playerBehavior = entityPlayer(0, 0)

# Instance (holes)
holes_sprite = pygame.image.load(sprites['holeOneSprite'])
holes_pos = pygame.Vector2(random.randint(
    0, config['width']), random.randint(0, config['height']))

# Instance (walls)
# wall_background_sprite = pygame.image.load(walls['background'])
# wall_background_pos = pygame.Vector2(100, 100)

clock = pygame.time.Clock()
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False

    screen.fill(colors['darkGreen'])
    holeBehavior = screen.blit(holes_sprite, holes_pos)
    screen.blit(playerBehavior.sprite, playerBehavior.pos)
    # wallBehavior = screen.blit(wall_background_sprite, wall_background_pos)
    # playerBehavior = screen.blit(player_sprite, player_pos)

    # Introduce [Collision]
    playerBehavior.checkCollision(holeBehavior)
    playerBehavior.move()
    pygame.display.update()
    clock.tick(60)
