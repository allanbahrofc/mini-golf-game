from scene_configuration import config, colors, sprites, walls, keys
import pygame
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
player_sprite = pygame.image.load('../res/sprites/Ball1.png')
player_pos = pygame.Vector2(config['windowMain'])

# Instance (holes)
holes_sprite = pygame.image.load('../res/sprites/Hole1.png')
holes_pos = pygame.Vector2(12, 12)

clock = pygame.time.Clock()
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                isRunning = False
            elif event.key == K_DOWN:
                player_pos.y -= 1
            elif event.key == K_UP:
                player_pos.y += 1
            elif event.key == K_LEFT:
                player_pos.x -= 1
            elif event.key == K_RIGHT:
                player_pos.x += 1

        elif event.type == QUIT:
            isRunning = False

        screen.fill(colors['darkGreen'])
        player = screen.blit(player_sprite, player_pos)
        hole = screen.blit(holes_sprite, holes_pos)
        pygame.display.update()
        clock.tick(60)
