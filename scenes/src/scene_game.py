import pygame
import random
from scene_configuration import config, colors, sprites, walls
from pygame.locals import *

pygame.init()
title = pygame.display.set_caption('Mini Golf')
screen = pygame.display.set_mode([config['width'], config['height']])

# Instance (player)
player_sprite = pygame.image.load(sprites['ballOneSprite'])
player_pos = pygame.Vector2(config['windowMain'])
player_dir = None
player_velocity = 0.4

# Instance (holes)
holes_sprite = pygame.image.load(sprites['holeOneSprite'])
holes_pos = pygame.Vector2(random.randint(
    0, config['width']-140), random.randint(0, config['height'])-120)

# Instance (walls)
wall_background_sprite = pygame.image.load(walls['background'])
wall_background_pos = pygame.Vector2(100, 100)

clock = pygame.time.Clock()
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False

    keys = pygame.key.get_pressed()

    # Keys
    if keys[K_UP] or keys[K_w]:
        player_dir = 'UP'

    elif keys[K_LEFT] or keys[K_a]:
        player_dir = 'LEFT'

    elif keys[K_RIGHT] or keys[K_d]:
        player_dir = 'RIGHT'

    elif keys[K_DOWN] or keys[K_s]:
        player_dir = 'DOWN'

    # Directions
    if player_dir == 'UP':
        player_pos.y -= 1*player_velocity
    elif player_dir == 'DOWN':
        player_pos.y += 1*player_velocity
    elif player_dir == 'LEFT':
        player_pos.x -= 1*player_velocity
    elif player_dir == 'RIGHT':
        player_pos.x += 1*player_velocity

    screen.fill(colors['darkGreen'])
    # wallBehavior = screen.blit(wall_background_sprite, wall_background_pos)
    holeBehavior = screen.blit(holes_sprite, holes_pos)
    playerBehavior = screen.blit(player_sprite, player_pos)
    # Introduce [Collision]
    if playerBehavior.collidepoint(holeBehavior.centerx, holeBehavior.centery):
        print('Collision')
    pygame.display.update()
    clock.tick(60)
