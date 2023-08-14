import entity.entityPlayer as entityPlayerBehavior
import entity.entityHole as entityHoleBehavior
import config
import pygame

# (Init)
pygame.init()

# (Default)
titleScreen = pygame.display.set_caption('Mini Golf')
clockFPS = pygame.time.Clock()
displayScreen = pygame.display.set_mode([config.window['width'], config.window['height']])

# (Prefab)
playerBehavior = entityPlayerBehavior.entityPlayer(50, 25)
holeBehavior = entityHoleBehavior.entityHole()

# (Loop)
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    displayScreen.fill(config.colors['darkGreen'])
    displayScreen.blit(holeBehavior.sprite, holeBehavior.pos)
    displayScreen.blit(playerBehavior.sprite, playerBehavior.pos)

    playerBehavior.movePlayer()
    playerBehavior.checkCollision(holeBehavior)
    pygame.display.update()
    clockFPS.tick(60)
    
