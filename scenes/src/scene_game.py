from scene_configuration import config, colors, sprites, walls
import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
title = pygame.display.set_caption('Mini Golf')
screen = pygame.display.set_mode([config['width'], config['height']])

# Instance (player)
player_sprite = pygame.image.load(sprites['ballOneSprite'])
player_pos = pygame.Vector2(config['windowMain'])

# Instance (holes)
holes_sprite = pygame.image.load(sprites['holeOneSprite'])
holes_pos = pygame.Vector2(random.randint(
    0, config['width']), random.randint(0, config['height']))

clock = pygame.time.Clock()
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                isRunning = False
            elif event.key == K_UP:
                player_pos.y -= 5*1.5
            elif event.key == K_DOWN:
                player_pos.y += 5*1.5
            elif event.key == K_LEFT:
                player_pos.x -= 5*1.5
            elif event.key == K_RIGHT:
                player_pos.x += 5*1.5

        elif event.type == QUIT:
            isRunning = False
        screen.fill(colors['darkGreen'])
        hole = screen.blit(holes_sprite, holes_pos)
        player = screen.blit(player_sprite, player_pos)
        
        if player.collidepoint(hole.centerx, hole.centery):
            print('Collision')
    pygame.display.update()
    clock.tick(60)
