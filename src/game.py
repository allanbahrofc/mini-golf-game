from pygame.locals import *
import config
import entity.entityPlayer as player
import pygame
import random

pygame.init()
title = pygame.display.set_caption('Mini Golf')
screen = pygame.display.set_mode([config.window['width'], config.window['height']])

# Instance (player)
playerBehavior = player.entityPlayer(50, 25)

# Instance (holes)
holes_sprite = pygame.image.load(config.sprites['holeOneSprite'])
holes_pos = pygame.Vector2(random.randint(
    0, config.window['width']), random.randint(0, config.window['height']))

# Instance (walls)
# wall_background_sprite = pygame.image.load(walls['background'])
# wall_background_pos = pygame.Vector2(100, 100)

clock = pygame.time.Clock()
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False

    screen.fill(config.colors['darkGreen'])
    holeBehavior = screen.blit(holes_sprite, holes_pos)
    screen.blit(playerBehavior.sprite, playerBehavior.pos)
    # wallBehavior = screen.blit(wall_background_sprite, wall_background_pos)
    # playerBehavior = screen.blit(player_sprite, player_pos)

    # Introduce [Collision]
    # playerBehavior.checkCollision(holeBehavior)
    playerBehavior.move()
    pygame.display.update()
    clock.tick(60)
