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
entityPlayerGroup = pygame.sprite.Group()
entityObstaclesGroup = pygame.sprite.Group()
playerBehavior = entityPlayerBehavior.entityPlayer()
holeBehavior = entityHoleBehavior.entityHole()

entityPlayerGroup.add(playerBehavior)
entityObstaclesGroup.add(holeBehavior)
# (Loop)
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        displayScreen.fill(config.colors['darkGreen'])
        playerBehavior.movePlayer()
        entityPlayerGroup.draw(displayScreen)
        entityObstaclesGroup.draw(displayScreen)
        pygame.display.flip()
        clockFPS.tick(60)
    
