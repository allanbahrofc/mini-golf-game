import pygame
import entity.entityPlayer as entityPlayerBehavior
import entity.entityHole as entityHoleBehavior
import config

pygame.init()
title = pygame.display.set_caption('Mini Golf')
screen = pygame.display.set_mode([config.window['width'], config.window['height']])

# Instance (entity)
playerBehavior = entityPlayerBehavior.entityPlayer(50, 25)
holeBehavior = entityHoleBehavior.entityHole()

clock = pygame.time.Clock()
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    screen.fill(config.colors['darkGreen'])
    screen.blit(holeBehavior.sprite, holeBehavior.pos)
    screen.blit(playerBehavior.sprite, playerBehavior.pos)

    playerBehavior.movePlayer()
    pygame.display.update()
    clock.tick(60)
